#include<stdio.h>
int main()
{
	int a[20];
	int i,j;
	int n;
	scanf("%d",&n);//所需输出的行数 
	if(n==1)//只有一行，输出即可 
		printf("1\n");
	else
	{
		a[0]=a[1]=a[2]=1;
		printf("1\n1    1\n"); //两行的话直接输出 
		for(i=3;i<=n;i++)//从第三行开始计算 
		{
			a[i-1]=1;//每行的最后一个数字都是1 
			for(j=i-2;j>0;j--)//倒着计算出每一行的数值 
				a[j]=a[j]+a[j-1];
			a[0]=1;//每行的第一个数字都是1 
		for(j=0;j<i;j++)//计算完一行，输出一行。 
			printf("%-5d",a[j]);
		printf("\n");
		}
	}
	return 0;
 } 
