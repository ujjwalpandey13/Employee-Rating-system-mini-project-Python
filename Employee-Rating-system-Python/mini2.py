import matplotlib.pyplot as plt

class EmployeePerformanceEvaluator:
    def __init__(self, filename):
        self.filename = filename
    
    def add_employee(self):
        employee_id = input("Enter employee ID: ")
        employee_name = input("Enter employee name: ")
        employee_designation = input("Enter employee designation: ")
        performance_rating = input("Enter performance rating: ")
        
        with open(self.filename, 'a') as file:
            file.write(f"{employee_id},{employee_name},{employee_designation},{performance_rating}\n")
        
        print("Employee evaluation added successfully.")
    
    def search_employee(self, employee_id):
        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == employee_id:
                    return data[1], data[2], data[3]
        
        return None
    
    def remove_employee(self, employee_id):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        with open(self.filename, 'w') as file:
            for line in lines:
                data = line.strip().split(',')
                if data[0] != employee_id:
                    file.write(line)

        print(f"Employee with ID {employee_id} removed successfully.")

# ...

    def generate_report(self):
        employee_ratings = {}
    
        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                employee_id = data[0]
                employee_name = data[1]
                employee_designation = data[2]
                rating = int(data[3])  # Convert rating to integer
                
                if employee_id in employee_ratings:
                    employee_ratings[employee_id].append(rating)
                else:
                    employee_ratings[employee_id] = [rating]
    
        print("Employee Performance Report:")
        for employee_id, ratings in employee_ratings.items():
            try:
                average_rating = sum(ratings) / len(ratings)
                liner = self.search_employee( employee_id)
                # print(f"Employee ID: {employee_id}, Average Rating: {average_rating:.2f}")
                print(f"Employee ID: {employee_id}, Employee name: {liner[0]}, Employee designation: {liner[1]}, Average Rating: {average_rating:.2f}")
            except ValueError:
                print(f"Invalid rating for employee {employee_id}. Skipping calculation.")
        # print(employee_ratings)
        


        # Plotting the performance graph
        x = list(employee_ratings.keys())
        y = [sum(ratings) / len(ratings) for ratings in employee_ratings.values()]
    
        plt.bar(x, y)
        plt.xlabel('Employee ID')
        plt.ylabel('Average Rating')
        plt.title('Employee Performance Report')
        plt.show()


    
    

evaluator = EmployeePerformanceEvaluator('employee1.txt')

while True:
    print("1. Add Employee Evaluation")
    print("2. Search Employee Evaluation")
    print("3. Remove Employee Evaluation")
    print("4. Generate Performance Report")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        evaluator.add_employee()
        print('---------------------------------------\n')
    elif choice == '2':
        employee_id = input("Enter employee ID to search: ")
        result = evaluator.search_employee(employee_id)
        if result is not None:
            employee_name, employee_designation, rating = result
            print(f"Employee ID: {employee_id}, Name: {employee_name}, Designation: {employee_designation}, Performance Rating: {rating}")
            print('---------------------------------------\n')
        else:
            print("No data found for the employee.")
            print('---------------------------------------\n')
    elif choice == '3':
        employee_id = input("Enter employee ID to remove: ")
        result = evaluator.search_employee(employee_id)
        if result is not None:
            employee_name, employee_designation, _ = result
            evaluator.remove_employee(employee_id)
            print(f"Employee with ID {employee_id}, Name: {employee_name}, Designation: {employee_designation} removed successfully.")
            print('---------------------------------------\n')
        else:
            print("No record of the employee")
            print('---------------------------------------\n')
        
    elif choice == '4':
        print('---------------------------------------\n')
        evaluator.generate_report()
        
        print('---------------------------------------\n')
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
        print('---------------------------------------\n')
