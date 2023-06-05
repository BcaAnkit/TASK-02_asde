import csv

def calculate_average_salary(department):
    salaries = [float(employee['Monthly Salary']) for employee in department]
    return sum(salaries) / len(salaries)

def generate_report(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        departments = {}
        for row in reader:
            department = row['DEPT_NAME']
            salary = float(row['MONTHLY_SALARY'])
            if department in departments:
                departments[department].append({'Monthly Salary': salary})
            else:
                departments[department] = [{'Monthly Salary': salary}]

        top_departments = sorted(departments.items(), key=lambda x: calculate_average_salary(x[1]), reverse=True)[:3]
        print('DEPT_NAME')
        print('AVG_MONTHLY_SALARY (USD)')
        for department, employees in top_departments:
            avg_salary = calculate_average_salary(employees)
            print(f'{department}')
            print(f'{avg_salary:.2f}\n')

csv_file = 'data.csv'  # Replace with the actual path to your CSV file
generate_report(csv_file)
