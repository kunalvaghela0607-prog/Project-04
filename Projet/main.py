data = []

def input_data():
    """Lets the user enter data as either a 1D list or a 2D list"""
    print()
    global data

    print("1. Make a 1D array")
    print("2. Make a 2D array")
    print()
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        data = input("Enter data for a 1D array (separated by spaces): ").split()
        data = list(map(int, data))
        print(data)
        print()
        print("Data has been stored successfully!")
        print()
        return data
        
    elif choice == 2:
        row = int(input("Enter the number of row: "))
        cols = int(input("Enter the number of columns: "))
        values = []
        for x in range(row):
            v = []
            for y in range(cols):
                num = int(input("Enter a value for 2D Array: "))
                v.append(num)
            values.append(v)
        
        print(values)
        return values
    else:
        print("invalid choice")
        return data

def conv(data):
    if len(data)>0  and isinstance(data[0],list):
        l =[]
        for x in data:
            l.extend(x)
        return l
    else:
        return data    

def display_data_summary(*data):
    """Shows a quick summary of the entered data"""    
    array_2d =conv(data)
    if not array_2d:
     print("No data available.")
     return

    print("Data summary: ")
    print(f"- Total elements: {len(array_2d)}")
    print(f"- Minimum value: {min(array_2d)}")
    print(f"- Maximum value: {max(array_2d)}")
    print(f"- Sum of all values: {sum(array_2d)}")
    print(f"- Average value: {round(sum(array_2d) / len(array_2d), 2)}")
    print()

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)

def factorial():
    """Finds the factorial of a given number with the help of recursion"""
    num = int(input("Enter a number to calculate its factorial: "))
    if num<=0:
        print("Factorial is not possible!")
        return 1
    
    ans = fact(num)
    print()
    print(f"Factorial of {num} is: {ans}")
    print()

def threshold_value(data):
    """Keeps only the values that meet a given threshold, using a lambda function"""
    l = conv(data)
    

    threshold_value = int(input("Enter the threshold value to filter out data above this value: "))
    threshold_data = list(filter(lambda x: x >= threshold_value, l)) 
    print(f"Filtered Data (values >= {threshold_value}): ")
    print(threshold_data)
    print()      

def sorting_data(data):
    """Arranges the data in either increasing or decreasing order"""
    l = conv(data)
    if len(l) == 0:
        print("No data available to sort.")
        return
    print("1. Ascending order")
    print("2. Descending order")
    print()
    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        l.sort()
        print("Sorted in Ascending Order: ")
        print()
        print(l)
        print()
    elif choice == 2:
        l.sort(reverse=True)
        print("Descending order")
        print(l)
        print()
    else:
        print("Invalid choice")

def calculate_data(data):
 
    l = conv(data)
    
    addition = sum(l)
    minimum = min(l)
    maximum = max(l)
    average = round(sum(l) / len(l), 2)
    return addition, minimum, maximum, average

def statistics_data(data):
     """Computes statistics of the dataset and returns several values together"""
    
     total_sum, min_val, max_val, avg_val = calculate_data(data)     
    
   
     return  total_sum, min_val, max_val, avg_val

def kwarg(**arb):
    for x, y in arb.items():
        print(y)
        
 

print("===== Welcome to the Data Analyzer and Transformer Program ! =====")
print()

while True:
    print("Main Menu: ")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()
    choice = int(input("Please Enter your choice from 1-7: "))
    print()
    if choice == 1:
        print(input_data.__doc__)
        data =input_data()

    elif choice == 2:
        print(display_data_summary.__doc__)
        print()
        display_data_summary(*data)

    elif choice == 3:
        print(factorial.__doc__)
        print()
        factorial()

    elif choice == 4:
        print(threshold_value.__doc__)
        print()
        threshold_value(data)

    elif choice == 5:
        print(sorting_data.__doc__)
        print()
        sorting_data(data)
 
    elif choice == 6:
        print(statistics_data.__doc__)
        print()
        if not conv(data):
            print("No data available.")
        else:
            total_sum, min_val, max_val, avg_val = statistics_data(data)
            kwarg(
                total_sum=f"Sum of All Values: {total_sum}",
                min_val=f"Minimum Value: {min_val}",
                max_val=f"Maximum Value: {max_val}",
                avg_val=f"Average Value: {avg_val}")
        print()

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice")