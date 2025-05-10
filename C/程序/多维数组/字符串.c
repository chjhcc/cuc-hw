#include<stdio.h>
#include<string.h>
int main(){
	char str[100];
	char b[100]; 
	printf("输入一个字符串:");
	scanf("%s",str);
	int i;
	int L;
	for(L=strlen(str);L>=0;L--)
	{
		for(i=0;i<=L;i++) 
		{
			b[i]=str[L]; 
		}
	};//构建中间字符串b 
	
	int temp,p;
	int O=strlen(b);
	for(p=0;p<O/2;p++)
	{
		temp=b[p];
		b[p]=b[O-1-p];
		b[O-1-p]=temp;
	}//将b倒转 
	
	printf("%s%s",str,b);
	return 0;
}
