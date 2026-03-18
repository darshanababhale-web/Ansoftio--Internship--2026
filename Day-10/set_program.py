numbers = input("Enter numbers separated by space: ")

num_list = list(map(int, numbers.split()))

unique_numbers = set(num_list)

print("Unique numbers are:", unique_numbers)
