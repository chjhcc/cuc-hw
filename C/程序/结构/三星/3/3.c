#include<stdio.h>
float w,h;
int main(){
	printf("Please input your weight(kg) and height(m):");
	scanf("%f %f",&w,&h);
	float t=w/(h*h);
	if(t<18)
	printf("low weight");
	else
	  {
	  	if(18<=t<25)
	  	printf("normal weight");
	  	else
	  	  {
	  	  	if(25<=t<27)
	  	  	printf("overweight");
	  	  	else
	  	    printf("overweight");
		  };
	  };
	return 0;
}
