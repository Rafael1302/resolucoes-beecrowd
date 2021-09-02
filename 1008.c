#include <stdio.h>

int main (){
int n=0, qtd_h=0;
float qtd_f=0, sal=0;

    scanf("%d", &n);
    scanf("%d", &qtd_h);
    scanf("%f", &qtd_f);

    sal = (qtd_h)*qtd_f;

    printf("NUMBER = %d\n", n);
    printf("SALARY = U$ %.2f\n", sal);

    return 0;
}
