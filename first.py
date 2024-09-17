#1. to print your name
# print("hello world")

# 2. to print your name using input
# name = input("enter your name")
# print(name)

# 3.WAP to find thr current age
# current_year =int(input("enter your current year"))
# born_year = int(input("enter your born year"))
# age = current_year - born_year
# print(age)

# 4.WAP for currency converter
# print("convert rupees into dollors")
# rupeesAmount = int(input("enter the amount in rs."))
# rsInDollor = (rupeesAmount/84)
# print(rupeesAmount,"convert into dollor",rsInDollor)

# 5. WAP for currency converter(dollor into rupees)
# print("convert dollor into rupees")
# dollorAmount = int(input("enter amount in dolllor"))
# dollorInRupees = (dollorAmount*84)
# print(dollorAmount,"convert into rs",dollorAmount)

# 6. WAP to check that you are elogible for vote or not
# userAge = int(input("enter your age"))
# if(userAge>17):
#     print("your eligible for voting")
# else:
#     print("you are not eligible for voting")
# userAge =int(input("enter your age"))
# gender = input("enter your gender")
# # method 1
# if(userAge>17 and gender == "female"):
#     print("your are eligible for govt job")
# elif(userAge>17 and gender == "male"):
#     print("you are elibble for private job")
# else:
#     print("you r not eligible for job")

# 7WAP to find greatest number among 3
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# num3 = int(input("enter third number"))
# if(num1>num2 and num1>num3):
#     print("num1 is greater")
# elif(num2>num1 and num2>num3):
#     print("num2 is greater")
# else:
#     print("num3 is greates")

# 8.list
# friendName = ["abhi","aman","ajay","akki"]
# # print before add name
# print("before",friendName)
# # to add the new friend in list
# friendName.append("raj")
# # print after adding name
# print("after",friendName)
# # to print the name in specific position
# friendName.insert(0,"harsh")
# friendName.insert(3,"harsh")
# # print after adding name at 0 index
# print("add name at the index 0",friendName)
# # to remove the name from the list
# friendName.remove("harsh")
# # print after removing name from the list
# print(friendName)
# # to clear the list
# friendName.clear()
# print(friendName)
# # to remove data in the list with specific index
# friendName.pop(3)
# print(friendName)
# # to sort the list
# friendName.sort()
# print(friendName)
# # to print element in the given list
# for names in friendName:
#     print(names)

# # 9.to print the no. 1 to 10
# for i  in range(1,11):
#     print(i)
    
# # 10.WAP to print thr even number.
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for num in list1:
#     if(num%2==0):
#         print(num)

# 11. set use to store the data and data is changable
# sets = {"aman","abhi","ajay","ritik"}
# sets.add("asad")
# sets.remove("asad")
# print(sets)
# print(type(sets))

# list1 = ["aman","abbhi","ajay","raj","asad"]
# print(list1)
# for i in list1:
#     print(i)
    
# # 12. WAP to use datetime
# import datetime
# x = datetime.datetime.now()
# print(x.month)

# from datetime import datetime
# birthDateInput = int(input("enter your birth date(YY-MM-DD)"))
# birthDate = datetime.strptime(birthDateInput,"%y-%m-%d")
# today = datetime.today()
# daysOld = (today-birthDate).days
# print(f"you are{daysOld} days old.")

# name = int(input("enter your name"))
# email = input("enter your mail")
# college = input("enter your college name")
# data = name + email + college
# f=open("abhi.txt","w")
# f.write(data)
# f.close()

# # 13 WAP to using while loop(break)
# i = 1
# while i<=10:
#     print(i)
#     breaki=i+1

# # (continue)
# i = 1
# while i<=10:
#     print(i)
#     i=i+1
#     continue

# # reverse
# 1=10
# while i>1:
#     print(i)
#     i=i-1
    
# # function in python
# # 14. create a function to print statement
# area = int(input("enter the area"))
# def myFunction(x,y):
#     return x*y
# print("area is",area)

# # call the function by name
# width = int(input("enter the width"))
# height = int(input("enter the height"))
# myFunction(width,height)
# print("the area is",area)

# tuple
# tuple can store the multiple data and data cant change
# myTuple = ("aman","abhi","ajay","aki")
# print(myTuple)
# print(type(myTuple))


# myTuple[1] = "aadars"
# print(myTuple)

# my_tuple = ("aman","ritik","roop")
# for value in my_tuple:
#     print(value)


# # Dictionary:
# # it can store multiple data in key value pair e.g.
# name = Abhi
# email = Abhi@gmail.com


# myDict = {
#     "name":"abhi tyagi",
#     "email":"abhi@gmail.com",
#     "mobile":"700000000"
# }
# print(myDict)

# for item in myDict:
#     print(myDict[item])    
# print(myDict.get("keys"))

# myDict["name"] = "aashish"
# print(myDict)

# # OOPS
# # class and object
# class Abhi:
#     age = 20 
#     print("im from delhi")
