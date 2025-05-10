#include <stdio.h>
#include <string.h>
#define SIZE 20
void deletechar( char s[],char c)
{	printf("原来字符串%s",s);
  //数组s删除指定字符
   printf("\n");
   char *p;
   for(p=s;*p!='\0';p++)
   	{if(*p!=c)
   			*s++=*p;
		   }	
	*s='\0';//字符串结束标志 
}

int main()
{
	char str[];
	int i;
	for(i=0;i<SIZE;i++)
	{
		scanf("%d",str[i]);
	}
	
  	char ch;
  	printf ("原始字符串:%s\n",str);
	printf("输入一个字符:");
	scanf("%c",&ch);
	deletechar(str,ch);
	printf("删除后是%s\n",str);
		return 0;
}

