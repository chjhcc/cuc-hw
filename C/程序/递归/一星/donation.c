#include <stdio.h>  
#include<math.h>
double total = 0.00;
double caculate(int amount);
int main() {
    int gross=1;
	  printf("\n");
      scanf("%d", &gross);
    while (gross > 0) 
	{
      double net = caculate(gross);
      printf("After expenses:\t$%.2lf\n",net);
      total += net;
      printf("Total raised:\t$%.2lf\n",total);
      printf("\n");
      scanf("%d", &gross);
    }
    printf("\n");
    return 0;
}
    double caculate(int amount) {
    const double NET_PERCENTAGE = 0.83;
    return(NET_PERCENTAGE * amount);
}
