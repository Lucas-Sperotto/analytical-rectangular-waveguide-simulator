#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <filesystem>
#include <vector>
#include <string>
#include <iomanip>

const double pi = M_PI;
const double c = 299792458.0;
const double mu0 = 4 * pi * 1e-7;
const double eps0 = 1.0 / (mu0 * c * c);

// Cria diretório se não existir
void criar_diretorio(const std::string& path) {
    std::filesystem::create_directories(path);
}

// Salva um campo escalar em CSV
void salvar_csv(const std::string& nome, const std::vector<std::vector<std::vector<double>>>& campo,
                double dx, double dy, double dz) {
    std::ofstream arq(nome);
    arq << "x,y,z,valor\n";
    int Nx = campo.size();
    int Ny = campo[0].size();
    int Nz = campo[0][0].size();
    for (int ix = 0; ix < Nx; ++ix) {
        for (int iy = 0; iy < Ny; ++iy) {
            for (int iz = 0; iz < Nz; ++iz) {
                arq << std::fixed << std::setprecision(6)
                    << ix * dx << "," << iy * dy << "," << iz * dz << ","
                    << campo[ix][iy][iz] << "\n";
            }
        }
    }
    arq.close();
}

int main() {
    // Parâmetros de simulação
    double a, b, Lz;
    int Nx, Ny, Nz;
    std::string caminho_csv = "data/frequencias/fc_lista.csv";

    std::cout << "Largura do guia (a) [m]: "; std::cin >> a;
    std::cout << "Altura do guia (b) [m]: "; std::cin >> b;
    std::cout << "Comprimento Lz [m]: "; std::cin >> Lz;
    std::cout << "Resolução (Nx Ny Nz): "; std::cin >> Nx >> Ny >> Nz;

    double dx = a / (Nx - 1);
    double dy = b / (Ny - 1);
    double dz = Lz / (Nz - 1);

    // Leitura do CSV de modos
    std::ifstream csv(caminho_csv);
    std::string linha;
    std::getline(csv, linha); // cabeçalho

    while (std::getline(csv, linha)) {
        std::istringstream ss(linha);
        std::string modo, tipo, sm, sn, sfc, skc, sbeta;
        std::getline(ss, modo, ',');
        std::getline(ss, tipo, ',');
        std::getline(ss, sm, ',');
        std::getline(ss, sn, ',');
        std::getline(ss, sfc, ',');
        std::getline(ss, skc, ',');
        std::getline(ss, sbeta, ',');

        int m = std::stoi(sm);
        int n = std::stoi(sn);
        double fc = std::stod(sfc);
        double kc = std::stod(skc);
        double beta = std::stod(sbeta);
        double H0 = 1.0;

        if (beta <= 0.0) continue; // não propaga

        // Cria diretório
        std::string pasta = "data/campos/" + modo + "/";
        criar_diretorio(pasta);

        // Inicializa campos
        std::vector<std::vector<std::vector<double>>> Ex(Nx, std::vector<std::vector<double>>(Ny, std::vector<double>(Nz, 0)));
        std::vector<std::vector<std::vector<double>>> Ey = Ex, Ez = Ex;
        std::vector<std::vector<std::vector<double>>> Hx = Ex, Hy = Ex, Hz = Ex;

        // Cálculo dos campos (modo TE)
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
                    double fase = cos(-beta * z); // tempo fixo

                    if (tipo == "TE") {
                        // Hz e derivadas
                        double Hz_val = H0 * cos_mx * cos_ny * fase;
                        double dHz_dx = -H0 * (m * pi / a) * sin_mx * cos_ny * fase;
                        double dHz_dy = -H0 * (n * pi / b) * cos_mx * sin_ny * fase;

                        Hz[ix][iy][iz] = Hz_val;
                        Ex[ix][iy][iz] = -(mu0 * 2 * pi * fc / (kc * kc)) * dHz_dy;
                        Ey[ix][iy][iz] = (mu0 * 2 * pi * fc / (kc * kc)) * dHz_dx;
                        Hx[ix][iy][iz] = -(beta / (kc * kc)) * dHz_dx;
                        Hy[ix][iy][iz] = -(beta / (kc * kc)) * dHz_dy;
                    }

                    if (tipo == "TM") {
                        // Ez e derivadas
                        double Ez_val = H0 * sin_mx * sin_ny * fase;
                        double dEz_dx = H0 * (m * pi / a) * cos_mx * sin_ny * fase;
                        double dEz_dy = H0 * (n * pi / b) * sin_mx * cos_ny * fase;

                        Ez[ix][iy][iz] = Ez_val;
                        Ex[ix][iy][iz] = -(beta / (kc * kc)) * dEz_dx;
                        Ey[ix][iy][iz] = -(beta / (kc * kc)) * dEz_dy;
                        Hx[ix][iy][iz] = (1 / (mu0 * 2 * pi * fc)) * dEz_dy;
                        Hy[ix][iy][iz] = -(1 / (mu0 * 2 * pi * fc)) * dEz_dx;
                    }
                }
            }
        }

        // Salvar arquivos
        if (tipo == "TE") {
            salvar_csv(pasta + "Ex.csv", Ex, dx, dy, dz);
            salvar_csv(pasta + "Ey.csv", Ey, dx, dy, dz);
            salvar_csv(pasta + "Hx.csv", Hx, dx, dy, dz);
            salvar_csv(pasta + "Hy.csv", Hy, dx, dy, dz);
            salvar_csv(pasta + "Hz.csv", Hz, dx, dy, dz);
        }
        if (tipo == "TM") {
            salvar_csv(pasta + "Ex.csv", Ex, dx, dy, dz);
            salvar_csv(pasta + "Ey.csv", Ey, dx, dy, dz);
            salvar_csv(pasta + "Hx.csv", Hx, dx, dy, dz);
            salvar_csv(pasta + "Hy.csv", Hy, dx, dy, dz);
            salvar_csv(pasta + "Ez.csv", Ez, dx, dy, dz);
        }

        std::cout << "Campos calculados para " << modo << "\n";
    }

    std::cout << "\nTodos os campos foram gerados!\n";
    return 0;
}
