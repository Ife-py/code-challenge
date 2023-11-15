def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'

    binary_representation = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_representation = str(remainder) + binary_representation
        decimal_number = decimal_number // 2

    return binary_representation

# Input decimal number
decimal_number = int(input("enter a number")) # Change this to your desired decimal number

# Convert the decimal number to binary
binary_representation = decimal_to_binary(decimal_number)

# Print the binary representation
print(binary_representation)
