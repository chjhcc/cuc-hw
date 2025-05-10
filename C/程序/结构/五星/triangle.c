#include<stdio.h>
float a,b,c;
int main(){
	printf("Please input three edges of the triangle:\n");
	scanf("%f %f %f",&a,&b,&c);
	float e=a*a,f=b*b,g=c*c;
	if(a<b+c&&b<a+c&&c<a+b)
	  {
	    if(a==b||b==c||a==c)
	    {
		  if(e-f-g<1e-1||f-e-g<1e-1||g-e-f<1e-1)
		  printf("为等腰直角三角形"); 
		  else
		  printf("为等腰三角形");
		}
		else
		  {
		  	if(e-f-g<1e-1||f-e-g<1e-1||g-e-f<1e-1)
		  	printf("是直角三角形");
			else
			printf("是一般三角形"); 
		  }
	  }
	else
	printf("不能构成三角形");
	return 0; 
} 
