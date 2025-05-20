import random
print("welcome to magic number ")
secret_number =random.randint(1,10)

while(1):
 number=input('please enter guess a number :')
 number=int(number)
 print(number)
 if(number==secret_number):
    print("how greate")
    break 
 elif(number>secret_number):
    print("the entered nubmer is larger")
 elif(number<secret_number):
    print("the enterd number is smallest")
