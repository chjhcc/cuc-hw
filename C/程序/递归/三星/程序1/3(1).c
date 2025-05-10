#include<stdio.h>
int AddTest(int a,int b){
	int Conclusion=a+b;
    return Conclusion;
} 
int main(){
	int num1,num2,input;
	scanf("%d %d",&num1,&num2);
	printf("Please enter the conclusion:%d+%d=",num1,num2);
    scanf("%d",&input);
    int result=AddTest(num1,num2);
    if(input==result)
    {
    	printf("Right!");
	}
	else
	printf("Not correct!Try again!");
	return 0;
}
