import os

class Student:
    name=""
    age=""
    gender=""

    def __init__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g


    def getData(self):
        return str(self.name+"\t"+self.age+"\t"+self.gender+"\n")

def generateId(total):
    sid=total
    n=0
    while(sid!=0):
        sid //= 10
        n+=1
    dig='0'*(3-n)
    return ("4MH19CS"+dig+str(total))

def getTotal():
    if('student.txt' not in os.listdir()):
        total=0
    else:
        total=0
        f=open('student.txt')
        for line in f:
            total+=1
    return total


def add(name,age,gender):
    total = getTotal()
    usn= generateId(total+1)
    '''print("Enter name:\t",end='')
    name=input()
    print("Enter age:\t",end='')
    age=input()
    print("Enter gender:\t",end='')
    gender=input()'''
    student = Student(name,age,gender)
    
    f=open("student.txt",'a+')
    f.write(str(usn)+"\t"+student.getData())
    f.close()

