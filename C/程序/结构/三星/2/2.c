#include<stdio.h>
float w,h;
int main(){
	printf("Please input your weight(kg) and height(m):");
	scanf("%f %f",&w,&h);
	float t=w/(h*h);
	if(t<=25)
	  {
	   if(t>=18)
	   printf("normal weight");
	   if(t<18)
	   printf("low weight");
	  };
	if(t>25)
	  {
	  	if(t<27)
	  	printf("overweight");
	  	if(t>=27)
	  	printf("fat");
	  };
	return 0;
}
