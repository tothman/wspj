def display_employee_details(name, job_title, gender, salary, years_of_experience):
    lines = [
        "Employee Name: " + name,
        "Job Title: " + job_title,
        "Gender: " + gender,
        "Salary: " + salary,
        "Years of Experience: " + str(years_of_experience)
    ]

    max_length = max(len(line) for line in lines)
    frame_line = "#" * (max_length + 4)  # Add padding

    print(frame_line)
    for line in lines:
        print("# " + line.ljust(max_length) + " #")
    print(frame_line)
    print()  # Add an empty line between employee cards for better readability


def load_employees(filename):
    employees = []
    with open(filename, 'r') as file:
        for line in file:
            # Assuming each attribute is separated by a comma
            details = line.strip().split(',')
            if len(details) == 5:  # Ensure there are exactly 5 attributes
                employees.append(details)
    return employees


# File containing employee information
filename = 'employees.txt'
employees = load_employees(filename)

# Display details for each employee

for employee in employees:
    display_employee_details(*employee)

