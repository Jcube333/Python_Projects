import datetime
today=datetime.datetime.now()
birthday = str(input("Enter your Birth date: "))
bday=datetime.datetime.strptime(birthday,"%d-%m-%Y")

print(bday,today)
bdayYear=bday.year
currYear=today.year
age=0


if int(bday.month)<int(today.month):
    age = int(currYear)-int(bdayYear)

elif int(bday.month)>int(today.month) :
        age = int(currYear)-int(bdayYear)-1

else :        
    if int(bday.day)<=int(today.day):
        age = int(currYear)-int(bdayYear)
    else:
        age = int(currYear)-int(bdayYear)-1 



print("Your age is "+ str(age) )