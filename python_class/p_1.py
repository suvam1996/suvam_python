class Student:
    def __init__(self, name, adress, phoneno):
        '''hello it is dockstring type,
        also a document type'''
        self.name = name
        self.adress = adress
        self.phoneno = phoneno
    def display(self):
        print(self.name,self.adress,self.phoneno)


s = Student(name='suvam', adress='odisha', phoneno=8917386210)
# print(s.name, s.adress, s.phoneno)
# s2 = Student(name='s', adress='f', phoneno=78888888888)
# print(s2.name, s2.adress, s2.phoneno)
s.display()

# s2 = Student('suvam','bbs',78955144)
# s2.display()
print(s.__doc__)
# help(Student)