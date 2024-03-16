#include <stdio.h>
void bitwiseOperations(int a, int b);
void bitwiseOperations(int a, int b) 
{
    printf("Bitwise AND: %d\n", (a & b));
    printf("Bitwise OR: %d\n",(a | b));
    printf("Bitwise XOR: %d\n",(a ^ b));
}

int main() 
{
    int n1, n2;
    printf("Enter first number: ");
    scanf("%d", &n1);

    printf("Enter second number: ");
    scanf("%d", &n2);
    bitwiseOperations(n1, n2);

    return 0;
}
