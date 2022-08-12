hungry = input("Are you hungry? (yes/no) \n")
if hungry=="yes":
    print("Have somthing to eat.")
    print("Have Itallian.")
    print("Have Chineeze.")
    print("Have Thai.")
elif hungry=="no":
    thirsty = input("Are you thirsty? (yes/no) \n")
    if thirsty == "yes":
        print("Have water.")
        print("Have soda.")
else:
    print("Answer in yes or no only.")