num=int(input("enter the number of lemons to give:"))
print("extra by {}".format(num-21) if num>21 else "less by {}".format(21-num) if num<21 else "sufficent")