import getpass
usr = {"Jcube333":"Jaimin@python","Pratham":"ABCD1234","Prakher":"Football@Messi"}

name=input("Enter your Username: ")
pswd=getpass.getpass("Enter you Password: ")

ct = 3
flgpwd=0
flgusr=0
for i,j in usr.items():

    if i==name:
        flgusr=1
        while ct!=-1:
            if j==pswd:
                print("User Authentictaed")
                flgpwd=1
                break
            else:
                if ct==0: 
                    ct=-1
                    continue
                print("Incorrect Password")
                pswd=getpass.getpass( str(ct)+" attempts remaining: " +"\nEnter password again: ")
                ct-=1
               
    if flgpwd:
        break 

if flgusr==0:
    print("User Doesn't exist ")
if ct==-1 and flgpwd==0:
    print("User Authentication Failed")    
        
