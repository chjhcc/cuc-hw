#include<stdio.h>
int main(){
    int m;
    int n=m%2;
	printf("please input m:");
	scanf("%d,%d",&m,&n);
	if(!n)
	  {if(m>0)
	     printf("%d is a positive even\n",m);
	     else
	      {if(m==0)
	       printf("%d is a even\n",m);
	       else
	       printf("%d is a negative even\n",m);
		  };
      }
    if(n)
     {if(m>0)
      printf("%d is a positive odd\n",m);
      else
      printf("%d is a negative odd\n",m);
	 };
	return 0;
}
