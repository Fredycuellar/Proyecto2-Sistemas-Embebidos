1.	#include <wiringPi.h>
2.	int main (void)
3.	{
4.	        wiringPiSetup();
5.	        pinMode(29, OUTPUT);
6.	        int i= 0;
7.	        for (i = 0;i<100;i++){
8.	                digitalWrite(29, HIGH);
9.	                delay(5000);
10.	                digitalWrite(29, LOW);
11.	                delay(5000);
12.	        }
13.	        return 0 ;
14.	}
