'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
import time
temp = 0
hum = 0
while(True):

    temp = random.random()*1000
    hum = random.random()*1000

    if(temp > 35 and hum < 30 ):
       
        print(" Warning!!! High Temperature !!!\n ")
        print("Temperature :  " + str(temp))
        print("Humidity : " + str(hum))
        print()
        
    elif(temp < 18 and hum > 45):
        
        print("Warning!!! Low Temperature!!!\n")
        print("Temperature :" + str(temp))
        print("Humidity : " + str(hum))
        print()
        
    elif((temp > 25 and temp >18) and (hum <30 and hum > 45)):
       
        print(" Normal ")
        print("Temperature : " + str(temp))
        print("Humidity :  " + str(hum))
        print()
        
    elif(temp < 18 and hum >50):
        
        print("High Alert !!! Extremely Low Temperature!!!\n")
        print("Temperature :" + str(temp))
        print("Humidity :" + str(hum))
        print()
    
    elif(temp >60 and hum < 25) :
       
        print("High Alert!!! Extremely High Temperature!!!\n")
        print("Temperature :" + str(temp))
        print("Humidity :" + str(hum))
        print()
    
    else:

        print("Fetching..........")
        
time.sleep(5)