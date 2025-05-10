#include<stdio.h>
void invert(int *a,int n)
{
  int *p,*pi,*pj;
  int temp,m;
  m=(n-1)/2;
  pi=a;
  pj=a+n-1;
  p=a+m;
  while(pi<=p)
  {
    temp=*pi;
    *pi=*pj;
    *pj=temp;
    ++pi;
    --pj;
  }
}

int main()

{
  int i;
  static int arr[]={1,2,3,4,5,6,7,8,9,10};
  for(i=0;i<10;i++)
    printf("%4d",arr[i]);
  printf("\n");
  invert(arr,10);
  for(i=0;i<10;i++)
    printf("%4d",arr[i]);
  printf("\n");
}
