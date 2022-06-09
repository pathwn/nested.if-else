age=int(input("enter age"))
sex=input("enter sex")
marital=input("are you marital")
if sex=="m":
    if age>=20 and age<=40 and marital=="yes":
        print("she may work any where")
    elif age>=40 and age<=60:
        print("she may work in urbon area")
    else:
        print("he was married")
elif sex=="f":
    if age>=20 and age<=40 and marital=="yes":
        print("she may work any where")
    elif age>=40 and age<=60:
        print("she will work in urbon area")
    else:
        print("ERROR")                            
                    
        