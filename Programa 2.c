	#include <wiringPi.h>
	int main (void)
	{
	        wiringPiSetup();
	        pinMode(29, OUTPUT);
	        int i= 0;
	        for (i = 0;i<100;i++){
	                digitalWrite(29, HIGH);
	                delay(5000);
	                digitalWrite(29, LOW);
	                delay(5000);
	        }
	        return 0 ;
	}
