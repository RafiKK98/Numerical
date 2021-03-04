tries = int(input("Enter number of integers to be taken (2 to 9) :"))
num_list = []
for n in range(tries):
    num = input("Enter a number to be taken :")
    num_list.append(num)

print("The list in reverse order :")
for n in range(len(num_list)):
    print(num_list[-1-n], end=" ")

