#create file:- syntax
#variablename=open("filename.extension","filename")
#eg.
# mylaptoppassword=open("passward.txt","w")

#write file:-syntax
#eg.
#mylaptoppassword.write("hui hui")

#read from file
#e.g.
#mylaptoppassword.read()

#delete file
#import os
# os.remove("password.txt")



#create file for saving my laptop password
#open function will create file
#when file is not exist and write the file
mypassword=open("password.txt","w")

#write a laptop password in file
mypassword.write("my macbook password-hui hui")


#overwrite the new password using underinput

mypassword.write(input("enter new password"))

#read the password from file
mypassword=open("password.txt","r")
mydata=mypassword.read()
if "macbook" in mydata:
    print("yes")
else:
    print("no") 
#to close the file
mypassword.close()       


#delete the file 
import os
os.remove("password.txt")

#create read write delete csv, excel, json,txt
#create csv file
mycsv=open("myfile.csv","w")
mycsv.write("pratham,vvo,ssd,aa,rr,")




myexcel=open("myexcel.xlxs","w")
myexcel.write("name,pawan,raman,anjali") 
