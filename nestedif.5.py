cat1=int(input("enter cat1"))
cat2=int(input("enter cat2"))
mouse=int(input("enter mouse"))
if cat1>mouse and cat2<mouse:
    print("cat1 will eat")
elif cat2<mouse and cat1<mouse:
    print("cat2 will eat")
elif cat1>=mouse and cat2<=mouse:
    print("mouse will escape")
else:
    print("not available")            