#include<stdio.h>
int a=2;
int f(int*a)
{
  return (*a)++;
}

int main()
{
  int s=0;
  {
    int a=5;
    s+=f(&a);
  }
  s+=f(&a);
  printf("%d\n",s);
}
