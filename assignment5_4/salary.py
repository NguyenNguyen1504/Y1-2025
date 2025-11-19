import math


def read_salaries():
    print("Enter the salaries of the summer one by one.\nStop by entering a negative value.")
    salary_list = []
    user_input = float(input())
    while user_input > 0:
        salary_list.append(user_input)
        user_input = float(input())
    return salary_list

def calculate_average(salary_list):
    total = 0.0
    for salary in salary_list:
        total += salary
    return total / len(salary_list)

def calculate_standard_deviation(salary_list):
    total = 0.0
    avg = calculate_average(salary_list)
    for salary in salary_list:
        total += (salary - avg) ** 2
    return math.sqrt(total / len(salary_list))

def calculate_salaries_below_limit(salary_list, upper_limit):
    count = 0
    for salary in salary_list:
        if salary < upper_limit:
            count += 1
    return count / len(salary_list) * 100

def calculate_salaries_over_limit(salary_list, lower_limit):
    count = 0
    for salary in salary_list:
        if salary > lower_limit:
            count += 1
    return count / len(salary_list) * 100

def main():
    print("The program calculates statistics for the salaries of students.")
    salary_list = read_salaries()
    print("Statistics (salary statistics for the entire summer): ")
    avg = calculate_average(salary_list)
    std_dev = calculate_standard_deviation(salary_list)
    below_limit = calculate_salaries_below_limit(salary_list, 3 / 4 * avg)
    upper_limit = calculate_salaries_over_limit(salary_list, 1.5 * avg)
    print(f"The average of the salaries is {avg:.2f} eur and")
    print(f"the standard deviation is {std_dev:.2f} eur.")
    print(f"{below_limit:.2f} % of students had a salary less than 75 % of the average.")
    print(f"{upper_limit:.2f} % of students had a salary at least 1.5 times larger than the average.")
    specify = float(input("Specify a salary limit to determine how many students exceed it.\n"))
    spe_upper = calculate_salaries_over_limit(salary_list, specify)
    print(f"{spe_upper:.2f} % of students earned more than {specify:.2f} euros.")

main()