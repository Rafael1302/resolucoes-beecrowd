#include <stdio.h>
#include <math.h>

int main(){
int R=0;
double vol=0, pi = 3.14159;

    scanf("%d", &R);

    vol = (4.0/3.0) * pi * pow(R,3);

    printf("VOLUME = %.3f\n", vol);

    return 0;
}
