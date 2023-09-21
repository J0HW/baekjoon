#include <stdio.h>
int main()
{
	int x, n;
	int a, b;
	int total = 0;
	scanf("%d\n %d\n", &x, &n);

	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d", &a, &b);
		total = total + (a * b);
	}

	if (x == total)
		printf("Yes");

	else
		printf("No");

	return 0;
}