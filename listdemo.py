# list can store multiple data, data can be different types int str
# list can store the dublicate data
# list is an ordered data set- sorting ascending descending

# create list and store your friend name
friendlist= ["rahul","mohit","don","wani"]

#print the list of friend names
print(friendlist)

# add the age of your friend in list
#append will add the data into end of the list
friendlist.append(36)
friendlist.append(26)
friendlist.append(21)
friendlist.append(22)

print(friendlist)

# add the data using index number
friendlist.insert(3,"pratham")
print(friendlist)
print(friendlist[3])


#access the complete list
for name in  friendlist:
    print(name)

# to delete the data from list
#remove will delete the data using value
friendlist.remove("pratham")
print(friendlist)


#pop will delete the data using index
friendlist.pop(1)
print(friendlist)


#add the 5 favt city name in list
#add my favt city kasol in  index 0
#remove tje last citu in list 
#sorting the data
#print the list data

favcity=["goa","ghaziabad","jaipur","bombay"]
favcity.insert(0,"kasol")
favcity.pop(3)
favcity.sort()
print(favcity)



