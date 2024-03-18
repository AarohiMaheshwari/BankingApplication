#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
void main()
{
  int gd=DETECT,gm,j;
  float i=0;
  initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

  for(i=1,j=1; i<=300,j<=200; i=i+0.4,j++)
  {
    circle(50+i,400-j,40);
    delay(10);
    cleardevice();
  }
  for(i=200,j=200; i<600,j<400; i=i+0.4,j++)
  {
    circle(50+i,j,40);
    delay(10);
    cleardevice();
  }
  circle(600,400,18);
  getch();
  closegraph();
}