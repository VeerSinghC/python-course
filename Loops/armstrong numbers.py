num = int(input("Enter a number: "))
num_str = str(num)
n = len(num_str)
armstrong_sum = sum(int(digit) ** n for digit in num_str)
if num == armstrong_sum:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
