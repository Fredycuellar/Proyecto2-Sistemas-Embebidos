	import time
	import serial
	import queue
	import threading
	import statistics
	import subprocess
	import board
	import busio
	import adafruit_adxl34x
	 
	port = None
	datoace = queue.Queue()
	mensaje = queue.Queue()
	 
	def main(Test):
	        global port
	        port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1)
	        threading.Thread(target=temp).start()
	        threading.Thread(target=acelerometro).start()
	        threading.Thread(target=recibir).start()
	        threading.Thread(target=enviar).start()
	        try:
	                while 1:
	                        time.sleep(1)
	        except:
	                port = None
	 
	def recibir():
	        x='a'
	        while 1:
	                if port.inWaiting() > 0:
	                        while port.inWaiting() > 0:
	                                #print('Leyendo dato')
	                                aux = port.read()
	                                x = x + str(aux)
	                                mensaje.put(x)
	                                print(x)
	                else:
	                        time.sleep(0.2)
	       
	       
	def enviar():
	        while 1:
	               
	                n= mensaje.get()
	                datos= n.split("-")
	                x = int(datos[1])
	                if datoace.empty():
	                        time.sleep(1)
	                else:
	                        for i in range (x):
	                                lista[i]= datoace.get()
	                        promedio= mean(lista)
	                        port.write(promedio)                   
	       
	       
	def temp():
	        while 1:
	                subprocess.call("./tempbash.sh")
	                time.sleep(1)
	 
	 
	def acelerometro():
	        i2c = busio.I2C(board.SCL, board.SDA)
	        accelerometer = adafruit_adxl34x.ADXL345(i2c)
	        while True:
	                datoace.put(accelerometer.acceleration)
	                time.sleep(1)
	               
	 
	 
	if __name__ == "__main__":
	        main("Hello")
