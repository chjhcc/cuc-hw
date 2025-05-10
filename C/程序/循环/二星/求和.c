#include<stdio.h>
int main() {
    double a,b,c,d;
	a=1;
	b=1;
	for (c=1;c>0;c++) 
	{
		d=1/(c+1);
		b=-b;
		a=a+b*d;
		if(d<1e-5)
		break;
	}
	printf("%.8Lf",a);
	return 0;
}

