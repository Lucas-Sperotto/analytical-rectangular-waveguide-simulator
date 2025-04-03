#include <iostream>
#include <fstream>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <iomanip>

const double pi = M_PI;
const double c = 299792458.0;
const double mu0 = 4 * pi * 1e-7;
const double eps0 = 1.0 / (mu0 * c * c);

using namespace std;

double calcular_beta(double omega, double kc) {
    double k0 = omega / c;
    return sqrt(k0 * k0 - kc * kc);
}

void salvar_csv(const string& nome, const vector<vector<vector<double>>>& campo,
                const string& header, double dx, double dy, double dz) {
    ofstream arq(nome);
    arq << "x,y,z," << header << "\n";

    int Nx = campo.size();
    int Ny = campo[0].size();
    int Nz = campo[0][0].size();

    for (int ix = 0; ix < Nx; ++ix) {
        for (int iy = 0; iy < Ny; ++iy) {
            for (int iz = 0; iz < Nz; ++iz) {
                arq << fixed << setprecision(6)
                    << ix * dx << "," << iy * dy << "," << iz * dz << ","
                    << campo[ix][iy][iz] << "\n";
            }
        }
    }

    arq.close();
}

int main() {
    double a, b, Lz, f;
    int m, n, Nx, Ny, Nz;

    cout << "Largura a [m]: "; cin >> a;
    cout << "Altura b [m]: "; cin >> b;
    cout << "Comprimento Lz [m]: "; cin >> Lz;
    cout << "Frequência [Hz]: "; cin >> f;
    cout << "Modo TE_mn (m n): "; cin >> m >> n;
    cout << "Resolução (Nx Ny Nz): "; cin >> Nx >> Ny >> Nz;

    double dx = a / (Nx - 1);
    double dy = b / (Ny - 1);
    double dz = Lz / (Nz - 1);

    double omega = 2 * pi * f;
    double kc = sqrt(pow(m * pi / a, 2) + pow(n * pi / b, 2));
    double beta = calcular_beta(omega, kc);
    double H0 = 1.0;

    // Campos
    vector<vector<vector<double>>> Ex(Nx, vector<vector<double>>(Ny, vector<double>(Nz)));
    vector<vector<vector<double>>> Ey(Nx, vector<vector<double>>(Ny, vector<double>(Nz)));
    vector<vector<vector<double>>> Hx(Nx, vector<vector<double>>(Ny, vector<double>(Nz)));
    vector<vector<vector<double>>> Hy(Nx, vector<vector<double>>(Ny, vector<double>(Nz)));
    vector<vector<vector<double>>> Hz(Nx, vector<vector<double>>(Ny, vector<double>(Nz)));

    // Preenchimento
    for (int ix = 0; ix < Nx; ++ix) {
        double x = ix * dx;
        for (int iy = 0; iy < Ny; ++iy) {
            double y = iy * dy;
            for (int iz = 0; iz < Nz; ++iz) {
                double z = iz * dz;
                double cos_mx = cos(m * pi * x / a);
                double sin_mx = sin(m * pi * x / a);
                double cos_ny = cos(n * pi * y / b);
                double sin_ny = sin(n * pi * y / b);
                double fase = cos(-beta * z); // tempo fixo (t = 0)

                // Campo longitudinal
                double Hz_val = H0 * cos_mx * cos_ny * fase;

                // Derivadas
                double dHz_dx = -H0 * (m * pi / a) * sin_mx * cos_ny * fase;
                double dHz_dy = -H0 * (n * pi / b) * cos_mx * sin_ny * fase;

                // Campos transversais
                double Ey_val = (omega * mu0 / (kc * kc)) * dHz_dx;
                double Ex_val = -(omega * mu0 / (kc * kc)) * dHz_dy;
                double Hx_val = -(beta / (kc * kc)) * dHz_dx;
                double Hy_val = -(beta / (kc * kc)) * dHz_dy;

                // Armazenar
                Ex[ix][iy][iz] = Ex_val;
                Ey[ix][iy][iz] = Ey_val;
                Hx[ix][iy][iz] = Hx_val;
                Hy[ix][iy][iz] = Hy_val;
                Hz[ix][iy][iz] = Hz_val;
            }
        }
    }

    // Salvar CSVs
    salvar_csv("fields_Ex.csv", Ex, "Ex", dx, dy, dz);
    salvar_csv("fields_Ey.csv", Ey, "Ey", dx, dy, dz);
    salvar_csv("fields_Hx.csv", Hx, "Hx", dx, dy, dz);
    salvar_csv("fields_Hy.csv", Hy, "Hy", dx, dy, dz);
    salvar_csv("fields_Hz.csv", Hz, "Hz", dx, dy, dz);

    cout << "Todos os campos TE_mn foram salvos com sucesso!\n";
    return 0;
}
