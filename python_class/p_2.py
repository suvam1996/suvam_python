# variables in class:

# 1.static variable
# 2.Non-Static variables
# 3.local variables


# methods in class:

# 1.staticmethod
# 2.non-staticmethod
# 3.classmethods
# -----------------------------------------------------------------
# 2.Non-Static variables / instance variable:
class Student:
    '''to use instance variable'''
    def __init__(self,name,rollno,mark):
        self.name= name
        self.rollno= rollno
        self.mark= mark
    def display(self):
        print('student name:',self.name)
        print('student rollno:',self.rollno)
        print('student mark',self.mark)

s=Student('Suvam Nayak',101,200)
s.display()








# class Student:
#     def __init__(self):
#         self.name= 'Suvam Nayak'
#         self.adress= 'Gabasahi,Bhadrak,Odisha'
#         self.pin= 756100
#
#
# s_info= Student()
# print(f'name:{s_info.name},Adress:{s_info.adress},Pin:{s_info.pin}')


