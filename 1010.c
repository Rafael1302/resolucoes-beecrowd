#include <stdio.h>

int main(){
int cod[2], u[2];
float preco[2], total;

    scanf("%d %d %f", &cod[1], &u[1], &preco[1]);
    scanf("%d %d %f", &cod[2], &u[2], &preco[2]);

    total = (u[1]*preco[1]) + (u[2]*preco[2]);

    printf("VALOR A PAGAR: R$ %.2f\n", total);

    return 0;
}
