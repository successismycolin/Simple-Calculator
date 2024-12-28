def run_calculator(string: str) -> float:
    """
        Runs calculation and returns its result

        Parameters:
            - A string that represents the numbers being calculated and the operator(s) 

        Returns:
            - A float that represents the result of the calculation
    """
    calculation = None
    result = 0

    for op in '+-/*':
        if op in string:
            list_nums = string.split(op) # A list of numbers in the string of the calculation
            result = float(list_nums[0]) + float(list_nums[1])


    return result

def divide():
    pass

def add():
    pass

def subtract():
    pass

def multiply():
    pass

print(run_calculator('4+5'))