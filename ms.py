import random

# Array size and number of each digit
size = 15
num_each_digit = size // 10 + 1

# Generate two arrays
digits = [i for i in range(10)] * num_each_digit
val_array = random.sample(digits, size)
test_array = random.sample(digits, size)

# Check same number in the same index
for i in range(size):
    if val_array[i] == test_array[i]:
        changeSw=True
        # Find a different number in the same index
        for j in range(i + 1, size):
            if test_array[j] != val_array[i] and test_array[j] != val_array[j]:
                test_array[i], test_array[j] = test_array[j], test_array[i]
                changeSw=False
                break
        if changeSw:
        # Can't find replace number in the array
            for j in range(0, i):
                if test_array[j] != val_array[i] and test_array[j] != val_array[j]:
                    test_array[i], test_array[j] = test_array[j], test_array[i]
                    changeSw=False
                    break
        if changeSw:
            print("Can't find replace number in the array")
            exit(0)

print(test_array)
print(val_array)