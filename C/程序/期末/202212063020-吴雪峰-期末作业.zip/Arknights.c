#include<stdio.h>
#include<string.h>
#include <stdlib.h>

#define num 15
#define length 10000 

int n=0,price=1; 

typedef struct The_users //存放用户注册信息的结构体   
{
    char id[11]; //账号 
    char pwd[20]; //密码 
}users;

void Create_File()//创建储存用户账号密码的文件
{
    FILE *fp;
    if ((fp = fopen("users.txt","rb"))==NULL)//如果此文件不存在
    {
        if ((fp = fopen("users.txt","wb+"))==NULL)
        {
            printf("无法建立文件！\n");
            exit(0);
        }
    }
}

struct The_CO //存放干员信息的结构体 
{
	char COname[num];//干员名字
	char COorg[num];//干员所属势力
	char COsex;
	char COjob[num];//干员职业 
	float number[9]; 
}CO[length]; 

void registers()//注册系统  
{    
    users a,b;//结构体 The_users 重命名定义
    FILE *fp;
    char temp[20];
    int count = 0;
    printf("欢迎来到注册界面！\n");
    Sleep(1000);
    fp = fopen("users.txt","r");
    
    fread(&b, sizeof(struct The_users), 1, fp); //读入一个结构体字符块 到b
    printf("请输入账号:\n");
    scanf("%s",&a.id);
         
	while (1)
    {    
        if (strcmp(a.id, b.id)) /*如果两串不相等*/
        {
            if (!feof(fp)) /*如果未到文件尾*/                                
            {
                fread(&b, sizeof(struct The_users), 1, fp);
            }
            else
            break;
            }
        else
		{   
            printf("此用户名已存在！请重新注册！\n"); 
            Sleep(1000);
            scanf("%s",&a.id);
			fclose(fp);
                
        }
    }
    
	printf("请输入密码:\n");
    scanf(" %s",&a.pwd);
    printf("请确认密码:\n");
    scanf(" %s",&temp);//密码设置 
	
	do
	{
      if(!strcmp(a.pwd,temp))
	  {
        fp = fopen("users.txt","a");
		fwrite(&a, sizeof(struct The_users), 1, fp);
		printf("账号注册成功，请登录！\n"); 
		Sleep(500);
		fclose(fp);
		return;
		}
	  else
	  {
	    printf("两次密码不匹配！请重新输入！\n");
		scanf("%s",&a.pwd);
		printf("请确认密码\n");
		scanf("%s",&temp);
	  }//确认密码 
	}while(1);
}
 
void  Input_login()//登录系统 
{
    users a,b;//定义结构体The_users别名
    
	FILE *fp;
    printf("欢迎来到登录界面！\n");
         Sleep(1000);
    fp = fopen("users.txt","r");

    fread(&b, sizeof(struct The_users), 1, fp); //读入一个结构体字符块 写入b
    printf("请输入账号:");
    scanf("%s",&a.id);   
    
    while (1)
    {   
	    if (strcmp(a.id, b.id)==0)         //如果有此用户名
	    {
	        break;       
	    }
	           
	    else 
	    {
	        if (!feof(fp))  //如果文件没有读完                            
	        {
	            fread(&b, sizeof(struct The_users), 1, fp);
	        }
	        else
	        {
	            printf("此用户名不存在，请重新输入！\n");
				Sleep(500); 
				fclose(fp);  
				scanf("%s",&a.id); 
				return;             
	        }
	    }
    }
    
	
	printf("请输入密码:");
    scanf("%s",&a.pwd); 
    do
	{   
	    if (strcmp(a.pwd, b.pwd)==0) /*如果密码匹配*/
	    {  
	        fclose(fp);
	        printf("登录成功,欢迎使用!");
	        Sleep(500);
	        return;
	    }
	    else  
	    {    
		    printf("密码不正确!请重新输入密码\n");
	       	scanf("%s",&a.pwd);         
	    }
	}
	while(strcmp(a.pwd, b.pwd)==0);   
}

void tuichu()//退出系统
{   
	int h;//控制是否确认退出 
	printf("即将退出，确认请按1，取消请按0:"); 
	scanf("%d",&h);
	if(h==1)
	{
		price=0; 
		printf("成功退出，感谢使用！\n");	
	}
	if(h==0)
	{
		printf("退出已取消！\n");
		system("pause");	
	}	
} 

void seek()//查询系统 
{
	int i,numb,flag;
	char s1[num+1];
	printf("1 按名字查询\n");
	printf("2 按势力查询\n");
	printf("3 按职业查询\n"); 
	printf("4 退出\n");

	while(1)
	{
		flag=0;
		printf("请选择你想要查询的项目：");
		scanf("%d",&numb);
		switch(numb)
		{
			case 1:
			printf("请输入需要查找干员的名字：\n");
			scanf("%s",s1);
			for(i = 0;i < n; i++)
			{
				if(strcmp(CO[i].COname,s1)==0)
				{
					flag=1;
					printf("名字\t\t势力\t\t职业\n");
					printf("%s\t\t%s\t\t%s\n",CO[i].COname,CO[i].COorg,CO[i].COjob);
				    printf("阻挡数:%d\n",CO[i].number[8]); 
				    printf("初始攻击\t\t初始防御\t\t初始血量\t\t初始法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[0],CO[i].number[1],CO[i].number[2],CO[i].number[3]);
					printf("毕业攻击\t\t毕业防御\t\t毕业血量\t\t毕业法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[4],CO[i].number[5],CO[i].number[6],CO[i].number[7]);
				}	
			}break;	
			
			case 2:
			printf("请输入需要查找干员的势力：\n");
			scanf("%s",s1);
			for(i=0;i<n;i++)
			{
				if(strcmp(CO[i].COorg,s1)==0)
				{
					flag=1;
					printf("名字\t\t势力\t\t职业\n");
					printf("%s\t\t%s\t\t%s\n",CO[i].COname,CO[i].COorg,CO[i].COjob);
				    printf("阻挡数:%d\n",CO[i].number[8]); 
				    printf("初始攻击\t\t初始防御\t\t初始血量\t\t初始法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[0],CO[i].number[1],CO[i].number[2],CO[i].number[3]);
					printf("毕业攻击\t\t毕业防御\t\t毕业血量\t\t毕业法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[4],CO[i].number[5],CO[i].number[6],CO[i].number[7]);
				}	
			}break;		
			
			case 3:
			printf("请输入需要查找干员的职业：\n");
			scanf("%s",s1);
			for(i=0;i<n;i++)
			{
				if(strcmp(CO[i].COjob,s1)==0)
				{
					printf("名字\t\t势力\t\t职业\n");
					printf("%s\t\t%s\t\t%s\n",CO[i].COname,CO[i].COorg,CO[i].COjob);
				    printf("阻挡数:%d\n",CO[i].number[8]); 
				    printf("初始攻击\t\t初始防御\t\t初始血量\t\t初始法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[0],CO[i].number[1],CO[i].number[2],CO[i].number[3]);
					printf("毕业攻击\t\t毕业防御\t\t毕业血量\t\t毕业法抗\n");
					printf("%f\t\t%f\t\t%f\t\t%f\n",CO[i].number[4],CO[i].number[5],CO[i].number[6],CO[i].number[7]);
				}	
		    }break;
		    
			case 4: return;
		}
		if(flag==0)
		printf("找不到该干员!\n请重新输入！"); 
	} 
} 

void Put_in()//录入程序 
{
	int i=n,j,flag,m=0;//i代表增加干员信息过程中任意时刻的干员数量 
	printf("请输入要录入的干员信息的数量：");
	scanf("%d",&m);
	if(m>0)
	{
	 for(i;i<n+m;i++)
	 {
		flag=1;
		while(flag)
		{
			flag=0;
			printf("请输入第%d位干员的名字：",i+1);
			scanf("%s",&CO[i].COname);
			//判断名字是否重复
			for(j=0;j<i;j++){
				if(strcmp(CO[i].COname,CO[j].COname)==0)
				{
					printf("该干员已经存在，请重新输入！\n");	
					flag=1;
					break;			
				}	 
			}
		}
		printf("请输入第%d位干员所属势力:",i+1);
		scanf("%s",&CO[i].COorg); 

		//处理上面输入的换行符，不然系统会把换行符当做一个字符赋值给性别 		
		printf("请输入第%d位干员性别:",i+1);
		scanf("%d",&CO[i].COsex);
 
		
		getchar(); 
		getchar();
		getchar(); 
		printf("请输入第%d位干员职业:",i+1);	
		scanf("%c",&CO[i].COjob);

		
		
		printf("请输入第%d位干员的初始攻击:",i+1);
		scanf("%f",&CO[i].number[0]);

		
		getchar();
		getchar();
		getchar();
		getchar();
		getchar(); 
		printf("请输入第%d位干员的初始防御:",i+1);
		scanf("%f",&CO[i].number[1]);

		
		getchar();
		printf("请输入第%d位干员的初始血量:",i+1);
		scanf("%f",&CO[i].number[2]);
		
		getchar();
		printf("请输入第%d位干员的初始法抗:",i+1);
		scanf("%f",&CO[i].number[3]); 

		
		getchar();
		printf("请输入第%d位干员的毕业攻击:",i+1);
		scanf("%f",&CO[i].number[4]);

		
		getchar();
		printf("请输入第%d位干员的毕业防御:",i+1);
		scanf("%f",&CO[i].number[5]);

		
		getchar();
		printf("请输入第%d位干员的毕业血量:",i+1);
		scanf("%f",&CO[i].number[6]);
		
		getchar();
		printf("请输入第%d位干员的毕业法抗:",i+1);
		scanf("%f",&CO[i].number[7]);
		
		getchar();
		printf("请输入第%d位干员的阻挡数:",i+1);
		scanf("%f",&CO[i].number[8]);
		}//只要当前干员人数还没到达添加后的总人数，就得继续添加		
	}
	n+=m;// 添加完成，系统人数n的值也要增加 
	printf("添加完成！！！\n");
	system("pause");
} 

void save()//把干员信息保存到文件 
{
	int i;
	FILE *fp;
	char filename[length+1];
	printf("请输入要保存的文件名：\n"); 	
	scanf("%s",filename);
	if((fp=fopen(filename,"w"))==NULL)
	{
		printf("打开文件失败！\n");
		exit(0);	
	}
	for(i=0;i<n;i++)
	if(fwrite(&CO[i],sizeof(struct The_CO),1,fp)!=1)
	printf("保存失败！！\n");
	printf("保存成功！！！\n");
	fclose(fp);
	system("pause");
}

void reset()//修改系统 
{
	int i,flag;
	char name[length],sex;
	char job[length];
	float  face[9];
	printf("请输入需要修改的干员名字：\n");
	getchar();
	gets(name);
	
	while(1)
	{	
		flag=0;
		for(i=0;i<n;i++)
		{
			if(strcmp(name,CO[i].COname)==0)
			{
				flag=1;
				int numb;//用于switch函数的子菜单 
				printf("1 修改名字\n");
				printf("2 修改性别\n");
				printf("3 修改职业\n");
				printf("4 修改势力\n");
				printf("5 修改面板\n");
				printf("6 退出\n");
				printf("请选择您想要进行的操作：");
				scanf("%d",&numb);
				switch(numb)
				{
					case 1:	
					  printf("请输入新的名字:\n");
					  getchar();
					  gets(name);
					  strcpy(CO[i].COname,name);break;
					case 2:
					  getchar();	
					  printf("请输入新的性别:\n");
					  scanf("%c",&sex);
					  CO[i].COsex=sex;break;
					case 3:
					  printf("请输入新的职业:\n");
					  getchar();
					  gets(job);
					  strcpy(CO[i].COjob,job);break;
                    case 4:
                      printf("请输入新的面板:\n"); 
					  printf("请输入新的初始攻击:");
					  scanf("%f",&face[0]);
					  CO[i].number[0]=face[0];
					  printf("请输入新的初始防御:");
					  scanf("%f",&face[1]);
					  CO[i].number[1]=face[1];
					  printf("请输入新的初始血量:");
					  scanf("%f",&face[2]);
					  CO[i].number[2]=face[2];
					  printf("请输入新的初始法抗:");
					  scanf("%f",&face[3]);
					  CO[i].number[3]=face[3];
					  printf("请输入新的毕业攻击:");
					  scanf("%f",&face[4]);
					  CO[i].number[4]=face[4];
					  printf("请输入新的毕业防御:");
					  scanf("%f",&face[5]);
					  CO[i].number[5]=face[5];
					  printf("请输入新的毕业血量:");
					  scanf("%f",&face[6]);
					  CO[i].number[6]=face[6];
					  printf("请输入新的毕业法抗:");
					  scanf("%f",&face[7]);
					  CO[i].number[7]=face[7];
					  printf("请输入新的阻挡数:");
					  scanf("%f",&face[8]);
					  CO[i].number[8]=face[8];
					case 5:
					return;break; 
				}
				if(num>0&&num<7)
				printf("修改成功，记得保存哟！！！\n");
				break;//找到干员，结束循环;	
			}
		}	
		if(flag==0)
		{
			printf("没有找到该干员，请重新输入需要修改信息的干员名字：\n");
			gets(name);
		}
	}
	system("pause");	
}

void del()//删除系统 
{
	int i,j,flag;
	char s1[length];
	printf("请输入需要删除的干员姓名：\n");
	scanf("%s",s1);
	flag=0;
	for(i=0;i<n;i++)
	{
		if(strcmp(s1,CO[i].COname)==0)
		{
			flag=1;
			for(j=i;j<n-1;j++)
			{
				CO[j]=CO[j+1];//直接把后面的干员都往前移动一位 
			}
		}
		if(flag==1) break;//说明已经找到了需要删除的干员，结束循环 
	} 
	 if(0==flag)
	 {
	 	printf("该干员不存在！！！\n");
	 }
	
	if(1==flag)
	{	
		printf("删除成功\n");
		n--;		
	}
	system("pause");
}

int main()
{	
    Create_File(); 
	int enter;
	printf("功能列表:\n");
	printf("1 注册并登录\n");
	printf("2 登录\n");
	printf("请选择您要进行的操作:");
	scanf("%d",&enter);
	switch(enter)//登陆部分;一级菜单
	{
		case 1:registers();
		       Input_login();break;
		case 2:Input_login();break;  
	} 
	
	int choice; 
	printf("功能列表:\n");
	printf("1 查询干员\n");
	printf("2 录入干员\n");
	printf("3 修改干员\n");
	printf("4 删除干员\n");
	printf("5 退出系统\n");
	
	
	while(price)
	{
		printf("请选择您要进行的操作:");
		scanf("%d",&choice);
	    switch(choice)
	    {
		  case 1:seek();break;
		  case 2:Put_in();
		         save();break;
		  case 3:reset();break;
		  case 4:del();break;
		  case 5:tuichu();break;
	    }//功能选择;二级菜单
	}
	return 0;
}
