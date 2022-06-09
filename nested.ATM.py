atm_card=input("insert the atm card")
if atm_card=="right side" or atm_card=="RIGFITSIDe":
    language=input("enter language")
    if language=="english" or language=="ENGLISH":
        language=="hindi" or language=="HINDI"
        pin=int(input("enter pin"))
        if pin>=1000 and pin<=9999:
            type_option=input("enter transaction option")
            if type_option=="withdraw" or type_option=="WITHDRAW":
                amount_type=input("enter amount_type")
                if amount_type=="saving" or amount_type=="SAVING":
                     key_name=input("enter ok")
                     amount=int(input("enter amount"))
                     if amount>=500 or amount<=2000 and amount%500==0:
                         a=amount//2000
                         b=amount%2000
                         c=a//500
                         d=b%500
                         print("notes of 2000=anotes of 500=c")    
                         amount_recept=input("enter amount_recept")
                         if amount_recept=="yes" or amount_recept=="no":
                             print("amount_recept")
                         else:
                             print("thank you for the transaction") 
            elif type_option=="balance equiry" or type_option=="BALANCEEQUIRY":
                amount_type=input("enter amount_type")
                account_no=int(input("enter account no"))
                key_name=input("enter ok")
                print("balance cheeking sucess full")
                if key_name=="ok" or key_name=="ok":
                    print("thank you sucess full enquiry")
                else:
                    print("thank you for the transaction")
            elif type_option=="balance equiry" or type_option=="BALANCE":
                amount_type=input("enter amount_type")
                account_no=int(input("enter account_no"))
                key_name=input("enter ok")
                print("balance cheeking sucess full")
                if key_name=="ok" or key_name=="ok":
                    print("thank you sucess full enquiry")
                else:
                    print("invalid enquiry")
            elif type_option=="balance enquiry" or type_option=="BaLANCEENQUIRY":
                amount_type=input("enter amount_type")
                account_no=int(input("enter account no"))
                key_name=input("enter ok")
                print("balance cheeking sucess full")
                if key_name=="ok" or key_name=="ok":
                    print("thank you sucess full enqiyry")
                else:
                    print("invalid enquiry")
            elif type_option=="deposide" or type_option=="DEPOSIDE":
                account_no=int(input("enter account_no"))
                if account_no>=1000000000000 and account_no<=999999999999:
                    bill_amount=int(input("enter bill_amount"))
                    if bill_amount>=1 and bill_amount<=1000000000000:
                        key_name=input("enter key_name")
                        if key_name=="ok" or key_name=="ok":
                            print(" sucess full")
                else:
                    print("not sucess full")
            elif type_option=="bill pay" and type_option=="BILLPAY":
                account_no=int(input("enter account_no"))
                if account_no>=1000000000000 and account_no<=999999999999:
                    bill_id=int(input("enter bill id number"))
                    if bill_id>=1000000000000 and bill_id<=999999999999:
                        press_key=input("enre press_key")
                        if press_key=="ok" and press_key=="ok":
                            print("bill transaction complet")
                        else:
                            print("press the ok batton") 
                    else:
                        print("wrong bill id") 
                else:
                    print("wrong account no")
            else:
                print("bengali language")
        else:
            print("wrong pin")
    else:
        print("atm left side")                
    
                                             