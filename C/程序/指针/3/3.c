#include <stdio.h>
int arr[3];
int *sort_three(int *a,int *b,int *c)
{
    int t;
	if(*a>*b)
	{	// 3 2 1
	  t=*a;	// t=3
	  *a=*b;	// a=2
	  *b=t;	// b=3
	}
	
	if(*a>*c)
	{
	  t=*a;	// t=2
	  *a=*c;	// a=1
	  *c=t;	// c=2
	}
	
	if(*b>*c)
	{
	  t=*b;	// t=3
	  *b=*c;	// b=2
	  *c=t;	// c=3
	}
	
	arr[0]=*a;
	arr[1]=*b;
	arr[2]=*c;
    return arr;
}

int main()
{
  int a,b,c;
  printf("enter 3 numbers:(a,b,c)");
  scanf("%d,%d,%d",&a,&b,&c);
  printf("origin:%d,%d,%d\n",a,b,c);
  sort_three(&a,&b,&c);
  printf("sort:%d,%d,%d\n",a,b,c);
  return 0;
}

