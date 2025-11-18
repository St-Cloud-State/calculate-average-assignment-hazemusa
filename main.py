# Haz Fa
# Assignment: Calculate Average of Three Scores
  # Instructions:
  # 1. Remove these comments after you understand the requested operation.
  # 2. Write the pseudocode as multi-line comments at the top. Include calling the function.
  # 3. Then write the Python code with comments explaining each line.

  # Call the function to test
def calculate_average(exam1,exam2,exam3):
    average = (exam1 + exam2 + exam3)/3
    print("The average is",average)


exam1 = float(input("Please enter the exam 1: "))
exam2 = float(input("Please enter the exam 2: "))
exam3 = float(input("Please enter the exam 3: "))

calculate_average(exam1,exam2,exam3)