exp_date=int(input("enter exp_date"))
exp_month=int(input("enter exp_month"))
exp_year=int(input("enter exp_year"))
return_date=int(input("enter return_date"))
return_month=int(input("enter return_month"))
return_year=int(input("enter return_year"))
if return_month==exp_month and return_year==exp_year:
    if return_date>=exp_date:
        days=exp_date-return_date
        fine=15*days
        print(fine)
    else:
        print("no charged")    
elif return_month>=exp_month and return_year==exp_year:
    if return_date>=exp_date:
        fine=500*30
        print(fine)
    else:
        print("fine charged")
elif return_month<=exp_month and return_year!=exp_year:
    if return_date<=exp_date:
        fixed_fine=10000
        print(fixed_fine)
    else:
        print("no fixed_fine")    
                           