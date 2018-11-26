#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>


//struct inventory {
//    	char name[20];
//    	int qty;
//};

struct customer {
    	char product_bought[20];
    	int qty;
    	char    cli_addr[16];
    	int  cli_port;
	char time[80];
    	struct customer *next;
};

struct customer *Create_Customer(){    // function to create a customer record node
   	struct customer *x =(struct customer *)malloc(sizeof(struct customer));
    	x->next=NULL;

    	return x;
}

int main(){

	/******** DS for time_stamping  *******/
	time_t     now;
    	struct tm *ts;
    	char buf[80];
    	
	/******** DS for time_stamping  *******/

	int listenfd = 0,connfd = 0,n=0,num=0;
    	struct sockaddr_in serv_addr;
    	struct sockaddr_in client_addr;

    	char sendBuff[1025];
    	char recvBuff[1024];
    	int numrv;
    	int mango=30, orange=30, guava=30, petrol=30 ,sav;
    	char new1[50];
    	int newn,i;

    	int bought=1;	//flag to check if any item was bought(default == 1)

    	listenfd = socket(AF_INET, SOCK_STREAM, 0);
    	printf("socket retrieve success\n");

    	memset(&serv_addr, '0', sizeof(serv_addr));
    	memset(sendBuff, '0', sizeof(sendBuff));

    	serv_addr.sin_family = AF_INET;
    	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    	serv_addr.sin_port = htons(5000);

    	bind(listenfd, (struct sockaddr*)&serv_addr,sizeof(serv_addr));

    	if(listen(listenfd, 10) == -1){
      		printf("Failed to listen\n");
      		return -1;
    	}

    	printf("\nAvailable items");
      	printf("\nProduct\tQuantity");
      	printf("\nMango\t%d", mango);
      	printf("\nOrange\t%d",orange);
      	printf("\nGuava\t%d",guava);
      	printf("\nPetrol\t%d",petrol);    

    	struct customer **Customers,*head,*temp;    
    	Customers = &head;

	int customer_count = 0;
    
    	while(1){

        	socklen_t addr_size = sizeof(client_addr);
        	connfd = accept(listenfd, (struct sockaddr*)&client_addr, &addr_size);	  // accept awaiting request

        	struct sockaddr_in* pV4Addr = (struct sockaddr_in*)&client_addr;
        	struct in_addr ipAddr = pV4Addr->sin_addr;	//.s_addr;

        	char str[INET_ADDRSTRLEN];      // this str contains client IPv4 address
        	inet_ntop( AF_INET, &ipAddr, str, INET_ADDRSTRLEN );

	 	

		/************** code to send the number of customers bought so far************/

		sprintf(sendBuff,"Number of Unique Customers so far: %d",customer_count);

		if ((send(connfd,sendBuff,strlen(sendBuff),0))== -1){
            		fprintf(stderr, "Failure Sending Message\n");
            		close(connfd);
            		break;
        	}

		/************** code to send the number of customers bought so far************/

		//read the data sent by client
        	num = recv(connfd, recvBuff, sizeof(recvBuff),0);
		now = time(NULL);///////////////////////////////////////////////////////////////////	//time-stamping
		ts = localtime(&now);
    		strftime(buf, sizeof(buf), "%a %Y-%m-%d %H:%M:%S %Z", ts);

        	if ( num <= 0 ){
            		printf("Either Connection Closed or Error\n");
        	}
        	recvBuff[num] = '\0';

        	for(i=1;i<strlen(recvBuff);i++){
            		new1[i-1]=recvBuff[i];
        	}
        	new1[i-1]='\0';
        	newn=atoi(new1);
                //printf("Server:Message Received From client -  %s\n",recvBuff);
        	if(recvBuff[0]=='m'){
            		sav=mango;
            		mango=mango-newn;
            		if(mango<0){
                		mango=sav;
                		printf("Requested quantity of Mango is not available");
                		bought=-1;
				sprintf(sendBuff,"Requested quantity of Mango is not available");
            		}
            		/* ------------------- logic of transaction entry ---------------- */
            		if(bought>0){
                		*Customers = Create_Customer();
				strcpy((*Customers)->product_bought,"Mango");	//product name
				(*Customers)->qty = newn;			//quantity
				strcpy((*Customers)->cli_addr,str);			//IP address
				(*Customers)->cli_port = client_addr.sin_port;	//Port No
				strcpy((*Customers)->time,buf);			//time_stamp value entered in the structure
				Customers=&((*Customers)->next);		//assigning the next address to the double pointer.
				customer_count++;
				sprintf(sendBuff,"Congratulations, transaction successfull");
		
            		}
            		/* ------------------- logic of transaction entry ---------------- */
        	}

        	if(recvBuff[0]=='o'){
            		sav=orange;
            		orange=orange-newn;
            		if(orange<0){
                		orange=sav;
                		printf("Requested quantity of Orange is not available");
				bought = -1;
				sprintf(sendBuff,"Requested quantity of Orange is not available");
            		}
			if(bought>0){
                		*Customers = Create_Customer();
				strcpy((*Customers)->product_bought,"Orange");
				(*Customers)->qty = newn;
				strcpy((*Customers)->cli_addr,str);
				(*Customers)->cli_port = client_addr.sin_port;
				strcpy((*Customers)->time,buf);
				Customers=&((*Customers)->next);
				customer_count++;
				sprintf(sendBuff,"Congratulations, transaction successfull");
            		}
        	}

        	if(recvBuff[0]=='g'){
            		sav=guava;
            		guava=guava-newn;
            		if(guava<0){
                		guava=sav;
                		printf("Requested quantity of Guava is not available");
				bought = -1;
				sprintf(sendBuff,"Requested quantity of Guava is not available");
            		}
			if(bought>0){
                		*Customers = Create_Customer();
				strcpy((*Customers)->product_bought,"Guava");
				(*Customers)->qty = newn;
				strcpy((*Customers)->cli_addr,str);
				(*Customers)->cli_port = client_addr.sin_port;
				strcpy((*Customers)->time,buf);
				Customers=&((*Customers)->next);
				customer_count++;
				sprintf(sendBuff,"Congratulations, transaction successfull");
            		}
        	}
        	if(recvBuff[0]=='p'){
            		sav=petrol;
            		petrol=petrol-newn;
            		if(petrol<0){
                		petrol=sav;
                		printf("Requested quantity of Petrol is not available");
				bought = -1;
				sprintf(sendBuff,"Requested quantity of Petrol is not available");
            		}
			if(bought>0){
                		*Customers = Create_Customer();
				strcpy((*Customers)->product_bought,"Petrol");
				(*Customers)->qty = newn;
				strcpy((*Customers)->cli_addr,str);
				(*Customers)->cli_port = client_addr.sin_port;
				strcpy((*Customers)->time,buf);
				Customers=&((*Customers)->next);
				customer_count++;
				sprintf(sendBuff,"Congratulations, transaction successfull");
            		}
        	}
        	//write the data for client
               //fgets(sendBuff,1025,stdin);

        	printf("\nMango\t%d\nOrange\t%d\nGuava\t%d\nPetrol\t%d\n",mango,orange,guava,petrol);
		
		// ========= Code to print Customers who already purchased ========	
		struct customer *t;
		t=head;
        	int x=0;
		while(t){
                	x++;
            		printf("\n===============%d===========",x);
            		printf("\nCustomer IP: %s",t->cli_addr);
            		printf("\nCustomer port: %d",t->cli_port);
            		printf("\nProduct Bought: %s",t->product_bought);
            		printf("\nQuantity Bought: %d",t->qty);
			printf("\nTime-Stamp: %s",t->time);
			printf("\n\n");
            		t=t->next;
        	}
		// ======== Code to print Customers who already purchased =========
		
		if ((send(connfd,sendBuff,strlen(sendBuff),0))== -1){
            		fprintf(stderr, "Failure Sending Message\n");
            		close(connfd);
            		break;
        	}   
        

               // printf("Server:Msg being sent: %s\nNumber of bytes sent: %d\n",sendBuff, strlen(sendBuff));


        	close(connfd); //Close Connection Socket
        	sleep(1);
    	} //End of Inner While...


return 0;
}

