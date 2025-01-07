import sys

def check_dread_pair(num_1: int, num_2: int) -> bool:
    """
    Check if the sum of two numbers invokes Dread.

    A pair of numbers invokes Dread if their sum is divisible by either 7 or 9, 
    but not both.
    """
    sum = num_1 + num_2 # get the total
    # check if the sum of the numbers are either divisible by 7 or nine
    div_by_7,  div_by_9 = sum % 7 == 0, sum % 9 == 0
    # return true if the total is either divisible by 7 and 9, but not both 
    if div_by_7 or div_by_9:
        return div_by_7 != div_by_9


def calculate_dread(input_data: list) -> int:
    """
    Calculate the overall Dread score for a list of integers based on Dread-invoking pairs.

    A pair invokes Dread if the sum  of the two numbers is divisible by either 7 or 9, but not both. The Dread score is the sum 
    of the sums of these Dread-invoking pairs, multiplied by the total number of such pairs.
    """
    
    # define variables to record the total of the dread pair and the number of dread pairs
    total_dread_pair = 0
    number_dread_pair = 0

    # determine the number of rows and columns in the input data
    rows = len(input_data)
    cols = len(input_data[0])

    # loop over each column
    for i in range(rows):
        for j in range(cols - 1):
            if check_dread_pair(input_data[i][j], input_data[i][j + 1]):
                total_dread_pair += input_data[i][j] + input_data[i][j + 1]
                number_dread_pair += 1

    # loop over each column
    for i in range(rows - 1):
        for j in range(cols):
            if check_dread_pair(input_data[i][j], input_data[i + 1][j]):
                total_dread_pair += input_data[i][j] + input_data[i + 1][j]
                number_dread_pair += 1

    # calculate the dread score
    dread_score = total_dread_pair * number_dread_pair
    return dread_score


input_data = []
try:
    with open(f'{sys.path[0]}/input_data.txt', 'r') as file:
        for line in file:
            input_data.append(list(map(int, line.strip().split(','))))

    # calculate the Dread score
    score = calculate_dread(input_data)

    # print the result
    print(f"The overall Dread score is: {score}")

except FileNotFoundError:
    print('The input file was not found')
