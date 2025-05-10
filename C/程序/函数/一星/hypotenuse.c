#include<stdio.h>
#include<math.h>
double hypotenuse(double a,double b)
{
	double result;
	result=sqrt(a*a+b*b);
	return result;
}
int main(){
	double e,f,length;
	printf("输入两直角边长：");
	scanf("%Lf %Lf",&e,&f);
	length=hypotenuse(e,f);
	printf("Hypotneuse:%.1Lf\n",length);
	return 0; 
}
