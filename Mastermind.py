import random
generated_number=""
for x in range(4):
    n=random.randint(1,6)
    generated_number+=str(n)
def Is_n_between_1_6(n):
    b=[]
    if len(str(n))>4:
        return False
    else:
        for x in str(n):
            if int(x)>=1 and int(x)<=6:
                b.append(True)
            else:
                b.append(False)
    if (False in b):
        return False
    else:
        return True
c=0
for x in range(10):
    n = int(input("Enter a number:"))
    while Is_n_between_1_6(n)==False:
        n = int(input("Enter a number (digits between 1 and 6/four digit number):"))
    result = ""
    for i,d in enumerate(str(n)):
        if (d in str(generated_number)) and str(generated_number)[i]==d:
            result+="+"
        elif (d in str(generated_number)) and str(generated_number)[i]!=d:
            result+="-"
        else:
            continue
    p = result.count("+")
    n = result.count("-")
    result = p * "+" + n * "-"
    if result.count("+")==4:
        print(result)
        break
    print(result)
    c+=1
if c<10:
    print("You won !")
else:
    print("You lost !")
    print("The number was:",generated_number)