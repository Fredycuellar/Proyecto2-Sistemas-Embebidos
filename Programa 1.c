#include <wiringPi.h>
	int main (void)
	{
	        wiringPiSetup();
	        pinMode(0, OUTPUT);
	        int i= 0;
	        for (i = 0;i<100;i++){
	                digitalWrite(0, HIGH);
	                delay(5000);
	                digitalWrite(0, LOW);
	                delay(5000);
	        }
	        return 0 ;
	}
