#include <stdio.h>
int main()
{
    int a, b, max = -10001, sum = 0;
    for (int i = 0; i < 4; i++)
    {
        scanf("%d %d", &a, &b);
        sum += -a + b;
        if (sum > max) max = sum;
    }
    printf("%d", max);
    return 0;
}