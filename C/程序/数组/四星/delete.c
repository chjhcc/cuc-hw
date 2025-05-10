#include <stdio.h>
int main()
{
    char str[100], c;
    int i, k = 0;
    printf("ÊäÈëÊı×é£º"); 
	gets(str);
    c = getchar();
    for (i = 0; str[i] != '\0'; i++)
    {
        if (str[i] != c)
        {
            str[k] = str[i];
            k++;
        }
    }
    str[k] = '\0';
    puts(str);
    return 0;
}


