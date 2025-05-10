#include<stdio.h>
int main(){
	int i;
	float a[9],max,min,sigma=0,final;
	for(i=0;i<9;i++)
	{
		printf("Please input %d trial's score:",i+1);
		scanf("%f",&a[i]);
		if(a[i]>=max)
		max=a[i];
		if(a[i]<=min)
		min=a[i];
		sigma=sigma+a[i];
		printf("\n");
	}
	final=(sigma-max-min)/7;
	printf("Your final score is %f\n",final);
	return 0;
}
