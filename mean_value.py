# 1) Store the given values:

# `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.
mean1=38
wrong_number=36
correct_number=56
total_number=40
# 2) Calculate the total sum using the wrong mean:

# - Multiply `mean1` by `total_number`

# - Store it in `sum`
sum=mean1*total_number
# - Print the sum.
print("the sum is",sum)
# 3) Fix the sum to get the correct total:

# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`
num2=sum-wrong_number+correct_number
# - Print the corrected sum.
print("the corrected sum is",num2)
# 4) Find the correct mean:

# - Divide `num2` by `total_number`
mean2=num2/total_number
# - Store it in `mean2`
print("mean2 value is:",mean2)
# - Print `mean2`.

