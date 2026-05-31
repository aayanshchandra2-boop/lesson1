amount=int(input("enter a withdrawl amount:"))
note_100=amount//100
r_amount=amount%100
note_50=r_amount//50
r_amount=r_amount%50
note_10=r_amount//10
print("number of 100 notes is:",note_100)
print("number of 50 notes is:",note_50)
print("number of 10 notes is:",note_10)
