#include<stdio.h>
char sex,sports,diet;
int Height,faHeight,moHeight;
int main(){
	printf("Please input your basic condition(sex,sports condition,diet,father's height,mother's height):\n");
    printf("(F-female,M-male;Y-like,N-dislike;Y-good,N-not good)\n");
	scanf("%c %c %c %d %d",&sex,&sports,&diet,&faHeight,&moHeight);
    if(sex=='F')
      {
      	if(sports=='Y')
      	  {
      	  	if(diet=='Y')
      	  	printf("%d\n",Height=(((faHeight)*0.923+moHeight)/2)*(1+0.02+0.015));
      	  	else
      	  	 printf("%d\n",Height=(((faHeight)*0.923+moHeight)/2)*(1+0.02));
				  }
		else
		    {
			  if(diet=='Y')
      	  	  printf("%d\n",Height=(((faHeight)*0.923+moHeight)/2)*(1+0.015));
      	  	  else
      	  	  printf("%d\n",Height=((faHeight)*0.923+moHeight)/2);
			};
	  }
	else
      {
      	if(sports=='Y')
      	  {
      	  	if(diet=='Y')
      	  	printf("%d\n",Height=((faHeight+moHeight)*0.54)*(1+0.02+0.015));
      	  	else
      	  	 printf("%d\n",Height=((faHeight+moHeight)*0.54)*(1+0.02));
				  }
		  else
		    {
			  if(diet=='Y')
      	  	  printf("%d\n",Height=((faHeight+moHeight)*0.54)*(1+0.015));
      	  	  else
      	  	  printf("%d\n",Height=(faHeight+moHeight)*0.54);
            }
	  };
	return 0;
}

