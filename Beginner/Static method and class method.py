## Static Method: A method that belongs to a class rather than any object from that class(instances)

# Instances methods= self.
#Static==  @static method

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f'{self.name}={self.position}' ###INstance method
# static method is just a regular function that lives inside a class body.
# # It doesn’t know about the instance (self) or the class (cls)—it’s “static” in that sense.
# #You use it when you want to bundle a helper function with a class, but it doesn’t need to read or modify any object- or class-specific data.

    @staticmethod
    def is_valid(position):
        valid_position=['Manager','Cashier','Cook','Janitor']
        return position in valid_position


print(Employee.is_valid('Cook'))

employee1=Employee('Songebob','Cashier')
print(employee1.get_info())
#######################################################################
print('#################################################')

## Static is when no Instances is required in class

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num +n

    @staticmethod
    def add(a,b):
        return a+b

print(f'addition is {Math.add(1,2)}')

a=Math(5)###num e jabe
print(a.num)
a.addtonum(6)
print(a.num)


# Class Method == Allow operation related to the class itself
#                  take (cls) as the first parameter, which represent the class itself

class Student:

    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa

        Student.count+=1 ### calculate the number of Student's object created

        Student.total_gpa+=gpa #### Total gpa created

    #INstannce method
    def get_info(self):
        return f'{self.name}=={self.gpa}'

    @classmethod
    def get_count(cls):
        return f'Total # of student {cls.count}'

    @classmethod
    def get_avg_gpa(cls):
        if cls.count==0:
            return 0

        else:
            return f'{cls.total_gpa / cls.count:.2f}'









student1=Student('Spongbob',3.56)
studdent2=Student('Wasmin',9.08)
print(student1.get_count()) #### Class call

print(student1.get_avg_gpa())

























