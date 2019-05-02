


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    

emp_1 = Employee('Tammy', 'Treit', 55000)
emp_2 = Employee('Wade', 'Reeves', 65000)

print (emp_1.fullname())
print (emp_2.fullname())

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Joe'
# emp_1.last = 'Thomas'
# emp_1.email = 'Joe.Thomas@comapny.com'
# emp_1.pay = 50000

# emp_2.first = 'Jane'
# emp_2.last = 'Thomas'
# emp_2.email = 'Jane.Thomas@comapny.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_1.pay)
# print(emp_2.email)
# print(emp_2.pay)