#include <stdio.h>
 int main()
{ char str[100],ch;  /*定义str字符串，定义ch用来存放要统计的字符*/
  int cnt=0,i;
  printf("请输入字符串：");    
  gets(str);
  printf("请输入要统计的字符：");
  scanf("%c",&ch);
  for( i=0;str[i];i++ )
     if( str[i]==ch )
         cnt++;    
  printf("字符串中%c字符的个数是：%d个",ch,cnt);
}
