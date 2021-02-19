'''Write a class Employee with name, age, job attributes, experience.
 Add method which calculates salary: basic_salary*(experience + job_coefficient)

Add method which calculates max experience valid for the job 
max_experience is reached when JOB_EFFICIENCE_COEF < current salary
and method which return if employee over experienced for the job'''

class Employee:

    BASIC_SALARY = 100

    JOB_SALARY_COEF = {
    'developer': 1.5,
    'devops': 2,
    'admin': 1.25,
    'pm': 2.5 }

    JOB_EFFICIENCE_COEF = {
    'developer': 1500,
    'devops': 2000,
    'admin': 800,
    'pm': 2100 }

    def __init__(self, name, age, job_attributes, experience):
        self.name = name
        self.age = age
        self.job_attributes = job_attributes
        self.experience = experience
    
    def calculate_salary(self):
        salary = self.BASIC_SALARY*(self.experience + self.JOB_EFFICIENCE_COEF[self.job_attributes])
        return salary

    def calculate_max_experience(self):

        if self.JOB_EFFICIENCE_COEF[self.job_attributes] < self.calculate_salary():
            return self.experience


employee1 = Employee("Bob", 43, "pm", 60000)

print(employee1.calculate_max_experience())