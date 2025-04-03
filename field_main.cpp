#include <iostream>
#include <cmath>
#include <complex>

const double pi = M_PI;
const double c = 299792458.0;
const double mu0 = 4 * pi * 1e-7;
const double eps0 = 1.0 / (mu0 * c * c);

// Função para calcular beta
double calcular_beta(double omega, double kc) {
    double k0 = omega / c;
    return sqrt(k0 * k0 - kc * kc);
}

int main() {
    double a = 0.02;  // largura [m]
    double b = 0.01;  // altura [m]
    double freq = 10e9; // frequência [Hz]
    double H0 = 1.0;  // amplitude do campo magnético
    double x = a / 2.0;
    double y = b / 2.0;
    double z = 0.0;
    double t = 0.0;

    double omega = 2 * pi * freq;
    double kc = pi / a;
    double beta = calcular_beta(omega, kc);

    std::complex<double> j(0, 1);
    std::complex<double> fase = std::exp(j * (omega * t - beta * z));
    double cos_kx = cos(pi * x / a);
    double sin_kx = sin(pi * x / a);

    // Campo Hz
    std::complex<double> Hz = H0 * cos_kx * fase;

    // Derivada parcial de Hz em relação a x: dHz/dx = -H0 * (pi/a) * sin(pi x / a)
    std::complex<double> dHz_dx = -H0 * (pi / a) * sin_kx * fase;

    // Campos elétricos
    std::complex<double> Ey = (j * omega * mu0 / (kc * kc)) * dHz_dx;
    std::complex<double> Ex = 0.0;
    std::complex<double> Ez = 0.0;

    // Campos magnéticos
    std::complex<double> Hx = -(beta / (kc * kc)) * dHz_dx;
    std::complex<double> Hy = 0.0;

    // Saída dos campos
    std::cout << "\nCampos no ponto (x=" << x << ", y=" << y << ", z=" << z << ", t=" << t << "):\n";
    std::cout << "Hz = " << Hz << "\n";
    std::cout << "Ey = " << Ey << " V/m\n";
    std::cout << "Hx = " << Hx << " A/m\n";

    return 0;
}
