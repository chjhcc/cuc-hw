#include<stdio.h>
#include<string.h>
int main()
{
    int i,j;
    char a[5][20], t[20];
    printf("ÊäÈë5¸ö×Ö·û´®:\n");
    for (i=0;i<5;i++)
    {
        scanf("%s",a[i]);
    }
    for (i=1;i<5;i++)
    {
        for (j=0;j<5-i;j++)
        if (strcmp(a[j], a[j+1]) > 0)
        {
        strcpy(t,a[j]);
        strcpy(a[j], a[j + 1]);
        strcpy(a[j + 1], t);
        }
    }
    printf("ÅÅÐòºó:\n");
    for (i = 0; i < 5; i++)
    puts(a[i]);
    return 0;

}

