#include <stdio.h>
int main() {
    char arr[1000];
    int a;
    scanf("%s %d", arr, &a);
    printf("%c", arr[a-1]);
    return 0;
}