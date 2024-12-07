#include <iostream>
#include <cctype>
using namespace std;

string formatear(string linea) {
    // Removemos espacios
    int inicio = linea.size();
    for (int i = 0; i < linea.size(); i++) {
        if (linea[i] != ' ') {
            inicio = i;
            break;
        }
    }
    int fin = -1;
    for (int i = linea.size() - 1; i >= 0; i--) {
        if (linea[i] != ' ') {
            fin = i;
            break;
        }
    }
    string mayusculas;
    for (int i = inicio; i <= fin; i++) {
        mayusculas += linea[i];
    }

    for (int i = 0; i < mayusculas.size(); i++) {
        mayusculas[i] = char(toupper(mayusculas[i]));
    }

    string sin_puntos;
    for (int i = 0; i < mayusculas.size(); i++) {
        if (mayusculas[i] != '.') {
            sin_puntos += mayusculas[i];
        }
    }

    string con_elipsis = sin_puntos + "...";
    return con_elipsis;
}

int main(void) {
    cout << formatear("           HoLa. . MuNdO.    ") << endl;
    return 0;
}