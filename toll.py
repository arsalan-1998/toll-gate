#from tkinter import *
from bluepy.btle import Scanner
import RPi
import time
import RPi.GPIO as GPIO
import mysql.connector
#import tkinter.messagebox

#mysql connection settings goes here....

con=mysql.connector.connect(
host='127.0.0.1',
user='root',
password='admin',
database='vehicle_details'
)
c=con.cursor()

#end of mysql connection....

#defination block for the bluetooth scan...

def sc():
    scne = Scanner()
    devices = scne.scan(0.5)
    return devices

#end .../
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(05,GPIO.OUT)

pwm=GPIO.PWM(05,100)
pwm.start(5)
angle1=10
duty1=float(angle1)/1+2.5
angle2=270
duty2=float(angle2)/10+2.5

#defination for the scanning of the bluetooth and operation of motor

def sca():
    de=sc()
    for dev in de:
        for i in range(1):
            print("Vehicle ID %s (%s)"%(dev.addr,dev.rssi))
            sql='select * from info'
            c.execute(sql)
            rec=c.fetchall()
            for r in rec:
                id=r[1]
                i=dev.addr
                if(id == i):
                    print("Vehicle ID:",r[1])
                    print("Registration No:",r[2])
                    print("Vehicle Type:",r[3])
                    print("Wallet Balance:",r[4])
                   # amt=r[4]
                #type=r[3].lower()
                #amt=r[4]
                #if(type == 'car'):
                   # print("rupess 50 has been deducted from your wallet")
                    #amt=amt-50
                    #print(amt)
                    #sql='''update info set amount='amt' where mac_addr=id '''
                    #c.execute(sql)
                    #con.commit()
                #else:
                   # print("rupees 100 has been deducted from your wallet")
                    #amt=amt-100
                    #print(amt)
                    #sql='''update info set amount='amt' where mac_addr=id '''
                    #c.execute(sql)
                    #con.commit()
            ck=0
            while ck<=0:
                pwm.ChangeDutyCycle(duty1)
	        time.sleep(30)
                pwm.ChangeDutyCycle(duty2)
	        time.sleep(30)
	        ck=ck+1
while True:
    sca()
