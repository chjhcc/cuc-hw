#include<stdio.h>
#include<string.h>
int main()
{
	char string[1024];
	int i, count = 0, flag = 0;
	char c;
	gets(string);  //读入一串字符串
	for(i=0; (c = string[i]) != '\0'; i++)
	{
		if(c==' ') flag = 0; //如果当前字符是空格，则使flag为0
		else if(flag == 0)
		{
			flag = 1;
			count++;
		}
	}
	printf("There are %d words in this line.\n",count);
	return 0;
}

