print("enter marks obtained in 5 subjects:")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
tot=mark1+mark2+mark3+mark4+mark5
avg=int(tot/5)
valid_range=range(0,101)
if avg not in valid_range:
    print("invalid input")

elif avg in range(91,101):
    print("a1")
elif avg in range(81,91):
    print("a2")
elif avg in range(71,81):
    print("b1")
elif avg in range(61,71):
    print("b2")
elif avg in range(51,61):
    print("c1")
elif avg in range(41,51):
    print("c2")
elif avg in range(33,41):
    print("d")
elif avg in range(21,33):
    print("e1") 
elif avg in range(0,21):
    print("e2")