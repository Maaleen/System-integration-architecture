#include <stdio.h>

int main() {
	//integer turultei 10 urttai husnegt zarlasan
	int a[10], i=0;	
	//file turultei maa, maa2 gesen haygan huvisagch uusgesen	
	FILE *MAA,*MAA2;
	//maa huvisagchid ma.txt file-iig read-r neej baina
	MAA=fopen("ma.txt","r");
	//maa2 huvisagchid hooson.txt file-g writh-r neesen
	MAA2=fopen("hooson.txt","w");
	//herev maa ni null baival..
	if(MAA==NULL)
		// cant open gej hevlene
	  	printf("cant open");
	else
		//i ni 10-s baga uyd doorh bagts code ajillana
	  	for(i=0;i<10;i++){
	  		//a husnegted maa file-s too unshij baina
		  	fscanf(MAA,"%d",&a[i]);
		  	//a husnegted unshsan toonuudaa 100-r urjuuleed maa2 t luu oruulna 
	     	fprintf(MAA2,"%d\n",a[i]*100);
     }
//neesen fileuudaa haaj baina 	
fclose(MAA);
fclose(MAA2);
}


