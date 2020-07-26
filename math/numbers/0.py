# Create a list of the numbers 34785, 76059, 52306, 80548 and print them out in
# expanded form
# E.g. 11111 => 10000 + 1000 + 100 + 10 + 1

ten_thousand = "asdasd"
thousand = "1000"
hundred = 100
ten = 454543
one = 2.456

multiples = [ten_thousand, thousand, hundred, ten, one]

# the following function prints numbers in expanded form
def multiply_numbers(number1, number2):
    pass


# tip python treats strings as if they're lists
def expand_number(num_list):
    """
        for each individual number in the NUMBER you're trying to expand
        (like how 12 has numbers 1 & 2)
        I want to create an array of numbers that represent each number
        so for 12 we should get [10, 2]
        We first create an array of numbers to add each number to
        We then have to treat our main NUMBER as if it was a list
        let's call it num_list from here on, it's still a number
        but we're treating it as if it's a list to get numbers from
        Remember what for loops dp
        Put a comment summarizing/explaining what for loops do here 👀

        
    """
    numbers = []
    for num in num_list:
        position = num_list.index(num)
        multiple = multiples[position]
        # create a function that multiplies numbers
        result = multiply_numbers(num * multiple)
        numbers.append(result)
    return numbers


expanded_numbers = expand_number(first)
