#include<stdio.h>
int n;
int main(){
	printf("Please input n:");
	scanf("%d",&n);
	int a,b,c,d;
	for(a=0;a<n;a++)
	{
		for(b=0;b<n;b++)
		{
			c=(a+b)%n;
			for(d=0;d<n;d++)
			{
				printf("%d",(c+d)%n+1);
			}
			printf("\n");
		}
		printf("\n");
	}
	return 0;
}
