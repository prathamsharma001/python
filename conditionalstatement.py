#conditional statement will check the condition is true or not
#to check the condition we use is else

#wap to check user eligible for voting
userage = int(input("enter your age "))
#note the default input function return type is string
#for vote userage must be greater than 18
if userage> 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting") 
       
gender= input("enter your gender")     
if gender =="male":
   print("you are not alloewd in 1 compartment ")
elif gender== "female":   
   print("you are alllowed in 1 compartment")
else:
    print("you sit any compartment")   

#wap if gender is female and age greater than 18-> govt job apply
# else male age greater than 18->private job apply

if gender == "female" and userage>18:
    print ("you are eligible for govt job")
elif gender== "male" and userage>18:
    print("ypu are eligible for private job")
else:
    print("you are not eligible")    

    