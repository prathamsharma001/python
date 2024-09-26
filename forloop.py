#for loop is udes to no. of iteration

username= "pratham sharma "

for  i in username:
     print(i)

#print 1 to 10 using for loop
for x in range(1,11):
     print(x)

#wap to create table of any no.

tableno= int(input("enter the number"))
for a in range(1,11)   :
     print(a * tableno)  

 # wap to print even no. 1 to 10 using for loop
 
for y in range(1,11):
     if y%2==0:
          print(y)

#wap print this pattern 1 4 7 10 13 using for loop
          
for b in range(1,14,3):
      print(b)          
    
 # wap print this pattern 1 3 7 11 13 15 using for loop

for w in range(1,16,2):
    if w== 9 or w== 5:
        continue #skip the current iteration
    else:
        print(w)
            