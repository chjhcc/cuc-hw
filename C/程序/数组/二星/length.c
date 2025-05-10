#include <stdio.h>
#include <string.h>
int main()
{
    int n,m,i,a;
    long L;
    printf("请输入数组长度：");
	scanf("%d",&a);
	char s[a];
    gets(s); 
	printf("输入数组s：");
	scanf("%c",&s);
    gets(s);
	printf("输入n和m："); 
	scanf("%d %d",&n,&m);
    L=a;
    if (n>0&&n<=L) 
	{
        for (i=n-1; i<=n+m; i++) 
		{
            printf("%c",s[i]);
        }
    } 
	else 
	{
        printf("起始位置%d越界",n);
    }
    return 0;
}
