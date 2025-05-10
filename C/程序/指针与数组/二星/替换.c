#include <stdio.h>
int main()
{
    int N;
    printf("enter N:");
	scanf("%d",&N);//读入数组个数 int array[N];
    int i,j;
    int nin,max,n=0,m=0;
	printf("enter %d data:",N); 
	int array[N];
	for(i=0;i<N;i++)
    {
        scanf("%d",&array[i]);
    }//读入数组 
    printf("origin:");
	for(i=0;i<N;i++)
    {
        printf("%d  ",array[i]);
    }
    printf("\n");
	nin=max=array[0];
    for(i=0;i<N;i++)
    {
        if(array[i]<nin)
        {
            n=i;
            nin=array[i];
        }
        if(array[i]>max)
        {
            m=i;
            max=array[i];
        }
    }
	int temp;
    temp=array[n];array[n]=array[0];array[0]=temp;
    int temp1;
    temp1=array[m];array[m]=array[N-1];array[N-1]=temp1;
    
	printf("max:%d\n",max);
    printf("min:%d\n",nin);
    printf("\n");
	
	printf("sorted:");
    for(i=0;i<N;i++)
    {
        printf("%d  ",array[i]);
    }
    return 0;
}
