#include <iostream>
#include <cmath>
#include <iomanip>

const double pi = M_PI;
const double c = 299792458.0; // velocidade da luz no vácuo [m/s]

// Função para calcular a frequência de corte (Hz) para o modo TE_mn ou TM_mn
double calcular_frequencia_corte(int m, int n, double a, double b) {
    double fc = (c / 2.0) * sqrt(pow(m / a, 2) + pow(n / b, 2));
    return fc;
}

int main() {
    double a, b;
    int modos = 3; // número de modos a exibir

    std::cout << "Digite a largura a [m] do guia de onda retangular: ";
    std::cin >> a;

    std::cout << "Digite a altura b [m] do guia de onda retangular: ";
    std::cin >> b;

    std::cout << "\nModos TE e TM (até ordem " << modos - 1 << "):\n";
    std::cout << std::fixed << std::setprecision(3);

    for (int m = 0; m < modos; ++m) {
        for (int n = 0; n < modos; ++n) {
            if (m == 0 && n == 0) continue; // modo TE_00 e TM_00 inexistentes

            double fc_TE = (m == 0 && n == 0) ? 0 : calcular_frequencia_corte(m, n, a, b);
            double fc_TM = (m == 0 || n == 0) ? 0 : calcular_frequencia_corte(m, n, a, b); // TM_0n e TM_m0 não existem

            std::cout << "TE_" << m << n << " -> fc = " << fc_TE / 1e9 << " GHz\t";
            if (fc_TM > 0)
                std::cout << "TM_" << m << n << " -> fc = " << fc_TM / 1e9 << " GHz";
            std::cout << "\n";
        }
    }

    return 0;
}
