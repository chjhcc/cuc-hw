#include <stdio.h>
int main()    
{              
	int i,j,k,m ; 
	for(i=0;i<=9;i++)
	{
		for(j=0;j<=9;j++)
		{
			if (i!=j)
			{
				k=i*1000+i*100+j*10+j;
				for(m=3;m*m<=k;m++)    
				{                                    
					if(m*m==k)
					{
						printf("³µÅÆºÅÎª%d\n",k);
					}
				}
			}
		}
	}
	return 0 ;
}
