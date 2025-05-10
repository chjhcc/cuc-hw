#include<stdio.h>
#include<string.h>
int f(char *s)
{ 
  int a,b;
  b=strlen(s);
  b--;
  for(a=0;a<b&&s[a]==s[b];a++,b--);
  if(a>=b)
   {
   	return 1;
   }
   else
   {
   	return 0;
   }
}


int main(){
  printf("输入一个不超过80个字符的字符串:");
  char s[80];
  gets(s);
  if(f(s)==1)
   printf("YES");
  else
   printf("NO");
  return 0;
}
