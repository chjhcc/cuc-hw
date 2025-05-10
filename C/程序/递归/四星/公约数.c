#include<stdio.h>

int CommonFactors(int a, int b);

int main()
{
	int sub,a,b;
	printf("Please input a and b:");
	scanf("%d%d",&a,&b);

	while((sub=CommonFactors(a, b)) > 0)
	{
		static int counter=1;
		printf("Common factor %d is %d\n",counter++,sub);
	}
	return 0;
}

int CommonFactors(int a, int b)
{
	int n=1;
    int i, cnt = 0;
    int temp;
    if(a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    for(i = a; i >= 1; i--)
    {
        if(a%i == 0 && b%i == 0)
            cnt++;
        if(n == cnt)
        return i;
    }
    return -1;
}
