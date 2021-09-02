#include <stdio.h>

int main() {
char nome;
double A,B;

    scanf("%s", &nome);
    scanf("%lf %lf", &A, &B);
    printf("TOTAL = R$ %.2f\n",( A + B * 0.15));

return 0;

}
