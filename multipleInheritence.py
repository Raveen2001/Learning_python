class Manager:
    def greet(self):
        print("Manager greets!!")


class Person:
    def greet(self):
        print("person greets!!")


class Employee(Person, Manager):
    pass


employee = Employee()
employee.greet()


#first the greet function is looked in Employee class then in Person then in Manager ..... so where the function is defined first gets executed remaining are not considered....