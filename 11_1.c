#include<stdio.h>
#include<math.h>
double x(double t,double u){
	return 3*cos(t)+cos(u)*cos(t);
}
double y(double t,double u){
	return 3*sin(t)+cos(u)*sin(t);
}
double z(double u){
	return sin(u);
}
int main(){
    int tc,uc,i=0;
    double t[50],u[50];
    FILE *f,*w;
    /*f = fopen("data.txt","a");
    for(temp=1;temp<=50;temp++){
   		fprintf(f,"%d %d\n",temp,temp);
    }
    fclose(f);*/
    f = fopen("data.txt","r");
    for(i=0;i<50;i++){
    	fscanf(f,"%lf %lf",&t[i],&u[i]);
	}  
    fclose(f);
    w = fopen("plot.txt","a");
    for(tc=0;tc<50;tc++){
    	for(uc=0;uc<50;uc++){
    		fprintf(w,"%lf %lf %lf\n",x(t[tc],u[uc]),y(t[tc],u[tc]),z(u[uc]));
		}
	}
    return 0;
}
