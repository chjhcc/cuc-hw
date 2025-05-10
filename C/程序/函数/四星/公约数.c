#include<stdio.h>
int MaxCommonFactor(int a,int b) 
{
    while(a!=b)
    {
        if(a>b)
        a = a - b;
        if(a<b)
        b = b - a;
    }
    return a;
}

int main(){
	int m,n,p;
	printf("输入两个正整数:");
	scanf("%d %d",&m,&n);
	
	p=MaxCommonFactor(m,n);
	
	printf("MaxCommonFactor=%d\n",p);
	return 0;
}
