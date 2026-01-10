from dataclasses import dataclass
from typing import List, Optional, override

@dataclass
class Person:
    name: str
    surname: str
    age: int
    email: Optional[str] = None

    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(self, name, surname, age)
        self.number = number
        print("Student sınıfı türetildi.")
        
    def study(self):
        print(f"{self.name} ders çalışıyor.")
    
    @override
    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(self, name, surname, age)
        self.branch = branch
        print("Teacher sınıfı türetildi.")

    def teach(self):
        print(f"{self.name} {self.branch} dersi anlatıyor.")

p1 = Person("Sadık","Turan",34)
p1.intro()

s1 = Student("Çınar", "x", 7, 321)
s1.intro()

t1 = Teacher("x", "y", 23, "x")
t1.intro()