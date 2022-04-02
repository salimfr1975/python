k,j,d=0,0,0
email = input("Enter your Email :")
if len(email )>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("space, upper case and digit not to be used in the begining.")
                else:
                    print("You entered the correct Email")
            else:
                print(". should be used 3rd or 4th place from last")
        else:
            print("@ should be used in Email 1 time in Email")
    else:
        print("The first letter of Email should start with character")
else:
    print("Your Email address is less then 6 character.")