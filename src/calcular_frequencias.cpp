#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <filesystem>

const double pi = M_PI;
const double c = 299792458.0;

// Cria pasta se não existir
void criar_diretorio(const std::string& path) {
    std::filesystem::create_directories(path);
}

int main() {
    double a, b, f;
    int m_max, n_max;
    std::string pasta = "data/frequencias/";
    criar_diretorio(pasta);

    std::cout << "Largura do guia (a) [m]: ";
    std::cin >> a;
    std::cout << "Altura do guia (b) [m]: ";
    std::cin >> b;
    std::cout << "Frequência de operação [Hz]: ";
    std::cin >> f;
    std::cout << "Modo máximo (m, n): ";
    std::cin >> m_max >> n_max;

    std::ofstream arq(pasta + "fc_lista.csv");
    arq << "modo,tipo,m,n,fc_Hz,kc,beta\n";
    arq << std::scientific << std::setprecision(6);

    double omega = 2 * pi * f;
    double k0 = omega / c;

    // Modos TE
    for (int m = 0; m <= m_max; ++m) {
        for (int n = 0; n <= n_max; ++n) {
            if (m == 0 && n == 0) continue;

            std::string nome = "TE" + std::to_string(m) + std::to_string(n);
            double kc = sqrt(pow(m * pi / a, 2) + pow(n * pi / b, 2));
            double fc = (c / (2 * pi)) * kc;
            double beta = (k0 > kc) ? sqrt(k0 * k0 - kc * kc) : 0.0;

            arq << nome << ",TE," << m << "," << n << "," << fc << "," << kc << "," << beta << "\n";
        }
    }

    // Modos TM (m > 0 e n > 0)
    for (int m = 1; m <= m_max; ++m) {
        for (int n = 1; n <= n_max; ++n) {
            std::string nome = "TM" + std::to_string(m) + std::to_string(n);
            double kc = sqrt(pow(m * pi / a, 2) + pow(n * pi / b, 2));
            double fc = (c / (2 * pi)) * kc;
            double beta = (k0 > kc) ? sqrt(k0 * k0 - kc * kc) : 0.0;

            arq << nome << ",TM," << m << "," << n << "," << fc << "," << kc << "," << beta << "\n";
        }
    }

    arq.close();
    std::cout << "Arquivo criado: " << pasta + "fc_lista.csv\n";
    return 0;
}
