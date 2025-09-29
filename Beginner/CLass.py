
class Car:
    def __init__(self,model,year,color,for_sale): ### contructor to create object like function
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f'You Drive the Car {self.model}')

    def stop(self):
        print(f'You Stop the Car {self.model}')




car1=Car('Ferrari',2025,'red',False)
car2=Car('Mustang',2012,'Black',True)
print(car1.model) ### with dot(.) accessing Attributes
print(car2.color)

car2.stop() ##### with function


###########################################################
# class Variable =  shared among all instance of class  (instance variable)
#                   Defined outside the constructor (class Variable) //// Allow to share Data among all the object created from that class
#
print('##################################################')

class Student:

    graduting_year=2029
    num_student=0

    def __init__(self,name,age):
        self.name=name#
        self.age=age
        Student.num_student+=1 #############

student1=Student('Fucknitosh',45)
student2=Student('t.f',67)

print(student2.age) ### instance variable
print(Student.graduting_year) ### class ariable can be accessed with name of class along with the oobect also

print(f'Number of objects created is:  {Student.num_student}')


########################################################
print('##################################################')

## Inheritance == Allows a class to inherit attributes and methods from another class
#                class child(Parent)



class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True ######## bolean


    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'Sleeping is {self.name}')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} can Barkk')

class Cat(Animal):
    pass

dog =Dog('Sccoby')

cat=Cat('Jingle')

dog.sleep()

print(cat.is_alive)

dog.speak()









