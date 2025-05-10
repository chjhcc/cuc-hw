# include <stdio.h>
int gcd(int a, int b)//递归函数 
{
	if(b%a==0)
		return a;
	else
		return gcd(b%a,a); 
}

int main()
{
	int m,n;
	int res, temp;
	printf("请输入两个整数，中间用空格隔开：");
	scanf("%d %d", &m, &n);
	if(m>n)//保证调用gcd函数时两个参数从小到大排列
	{
		temp=m;
		m=n;
		n=temp;
	} 
	res=gcd(m,n);
	printf("%d和%d之间的最大公约数是%d。\n",m, n, res); 
	return 0;
}

