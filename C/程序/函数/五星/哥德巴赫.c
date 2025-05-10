#include<stdio.h>
#include<math.h>
int prime(int n)//判断素数 
{
	int i,k,L;
	k = sqrt(n);
	for(i=2;i<=k;i++)
		if(n%i==0)
			break;
	if(i<=k)
	L=0;
	else
	L=1; 
    return L;
}
void judge(int a)//判断猜想 
{
	int e,f;
	for(e=2;e<=a;e++)
	{
	 for(f=2;f<=a;f++)
	 if(e+f==a)
	 {
	 	if(prime(e))
		 {
		 	if(prime(f))
		 	printf("%d=%d+%d\n",a,e,f); 
		  } 
	  } 
	}
 } 
 int main(){
 	int m;
	printf("请输入一个不小于6的偶数:");
 	scanf("%d",&m);
	if(m%2==0)
	{
		if(m>=6)
		{
			judge(m);
		}//正常输入 
		else
		printf("输入数据非法");
	  }  
	  else
	  printf("输入数据非法");
	return 0;
 }
