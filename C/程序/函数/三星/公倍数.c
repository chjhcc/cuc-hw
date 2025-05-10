#include<stdio.h>
int MinCommonMultiple(int a,int b)
{
	int result;
   for(result=1;;result++)
   {
       if(result%a==0&&result%b==0)
       {
           return result;
       }
   }
}
int main(){
	int m,n,p;
	printf("输入两个正整数:");
	scanf("%d %d",&m,&n);
	p=MinCommonMultiple(m,n);
	printf("p=%d\n",p);
	return 0;
}
