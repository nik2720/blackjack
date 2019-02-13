'''
Created on Feb 10, 2019

@author: Nik
'''
import time 
import random 

faces = {'king':10,'queen':10,'jack': 10 ,'ace': 1   , 'two': 2 , 'three':3, 'four': 4, 'five': 5 ,'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten':10}
suite = ['spades', 'hearts', 'diamonds', 'clubs']

total=[]

def turn2():
    keyfaces3 = random.choice(list(faces))
    keysuite3 = random.choice(list(suite))
    if keyfaces3 == 'ace':
        print('you drew an ace')
        print('do you want to use the value of 1 or 11?')
        z=0
        while z!=1:
            user=int(input())
            
            for key, value in faces.items():
               
                if user == 1:
                    z=1
                    if value == 1:
                        thirdcard_total_1=1
                        total.append(thirdcard_total_1)
                    
                elif user == 11:
                    z=1
                    if value == 1:
                        thirdcard_total_11=11
                        total.append(thirdcard_total_11) 
                   
    elif keyfaces3 != 'ace':
        thirdcard_total=(faces.get(keyfaces3,0))
        total.append(thirdcard_total)  
    
    total_value=sum(total)
  
    print ((keyfaces3) + ' of ' + (keysuite3))
           
    if total_value == 21:
        print(total_value)
        print('congratulations you have reached the max number')
        restart()
    
    elif total_value > 21:
        print(total_value)
        print('your total was too high')
        restart()
    
    else:
        print(total_value)
        hitorstand()    
 
def restart():
    time.sleep(2)
    print('game over')
    time.sleep(1)
    print('do you want to play again?')
    time.sleep(1)
    print('enter y to play again')
    print('enter n to quit')
    user=str.lower(input())
    if user == 'y':
        total.clear()
        randomface(faces)
        
    elif user == 'n':
        exit()
    
    else:
        print('that was an invalid command')
        restart()

def stand():
    global total_value 
    total_value=sum(total)
    
    if total_value > 21:
        print('you lose')
        print('total')
       
        print(total_value)
        restart()
        
    elif total_value < 21:
  
        print('total')
        print(total_value )
        restart()
    
    elif total_value == 21:
        print('congratulations you have reached the max number')
        print('total')
        print(total_value )
        restart()
    
    else:
        hitorstand()  
 
def hitorstand():
    time.sleep(1)
    print('')
    print('do you want to hit or stand?')
    print('enter h to hit')
    print('enter s to stand')
   
    user=str.lower(input())
    if user == 'h':

        turn2()
    elif user == 's':
        stand()
    else:
        print('that was an invalid command')
        hitorstand()

def randomface(faces):
    keyfaces = random.choice(list(faces))
    keysuite = random.choice(list(suite))
    
    if keyfaces == 'ace':
        print('you drew an ace')
        print('do you want to use the value of 1 or 11?')
        x=0
        while x!=1:
            user=int(input())
            for key, value in faces.items():
                if user == 1:
                    x=1
                    if value == 1:
                        firstcard_total_1=1
                        total.append(firstcard_total_1)
                       
                    
                elif user == 11:
                    x=1
                    if value == 1:
                        firstcard_total_11=11
                        total.append(firstcard_total_11)
    elif keyfaces != 'ace':
        firstcard_total =(faces.get(keyfaces,0)) 
        total.append(firstcard_total)
  
    print ((keyfaces) + ' of ' + (keysuite))    
    
    keyfaces2 = random.choice(list(faces))
    keysuite2 = random.choice(list(suite))
    print('')
    if keyfaces2 == 'ace':
        print('you drew an ace')
        print('do you want to use the value of 1 or 11?')
   
        y=0
        while y !=1:
            user=int(input())
            for key, value in faces.items():
                if user == 1:
                    y=1
                    if value == 1:
                        secondcard_total_1=1
                        total.append(secondcard_total_1)
              
                elif user == 11:
                    y=1
                    if value == 1:
                      
                        secondcard_total_11=11
                        total.append(secondcard_total_11)
                       

    elif keyfaces2 != 'ace':
        secondcard_total=(faces.get(keyfaces2,0))
        total.append(secondcard_total)
            
    print ((keyfaces2) + ' of ' + (keysuite2))   
        
    total_value=sum(total)    
    print('Total')
    print(total_value)
    if total_value == 21:
        restart()
        print('congratulations you have reached the max number')
    
    elif total_value > 21:
        restart()
        print('your total was too high')
     
    else:
        hitorstand()
x=0    
while x <=52:
    x+1
    randomface(faces)