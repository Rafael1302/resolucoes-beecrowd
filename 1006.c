#include <stdio.h>

int main(){
float A=0, B=0, C=0, MEDIA=0;

    scanf("%f", &A);
    scanf("%f", &B);
    scanf("%f", &C);

    MEDIA =(((A*2)+(B*3)+(C*5))/10);

    printf("MEDIA = %.1f\n", MEDIA);

    return 0;
}

