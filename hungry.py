hungry = input("Are you hungry? (yes/no) \n")
if hungry=="yes":
    print("Have somthing to eat.")
    print("Have Itallian.")
    print("Have Chineeze.")
elif hungry=="no":
    thirsty = input("Are you thirsty? (yes/no) \n")
    if thirsty == "yes":
        print("Have water.")
else:
    print("Answer in yes or no only.")