#include<stdio.h>
int AddTest(int a,int b){
	int Conclusion=a+b;
    return Conclusion;
} 
int main(){
	int num1,num2,input,i;
	scanf("%d %d",&num1,&num2);
	printf("Please enter the conclusion:%d+%d=",num1,num2);
    scanf("%d",&input);
    int result=AddTest(num1,num2);
    for(i=1;;i++)
    {
    	if(input==result)
    	{
    		printf("Right!");
		    break;
		}
		else
		{
			if(i<=2)
            {
                printf("Not right!Try again!"); 
			    scanf("%d",&input);
			}
			else
			{
				printf("Not right!Test over");
				break;
			}
		}
	}
	return 0;
}
