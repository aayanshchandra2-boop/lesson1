# 1) Ask the user to enter the numerator and store it in `numn`.

# 2) Ask the user to enter the denominator and store it in `numd`.

# 3) Check if `numn` is divisible by `numd`:

# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.



numn=int(input("enter numerator:,sotre it in numn"))
numd=int(input("enter denominator:,store it in numd"))
if numn%numd==0:
    print(numn,"is divisible by",numd)
else:
    print(numn,"is not divisible by",numd)
 