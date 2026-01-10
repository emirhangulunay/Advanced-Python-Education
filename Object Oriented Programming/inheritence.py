from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Person:
    name: str
    surname: str
    age: int
    email: Optional[str] = None

    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    pass

class Teacher(Person):
    pass


p1 = Person("Sadık","Turan",34)
p1.intro()

s1 = Student("Çınar", "x", 7)
s1.intro()

t1 = Teacher("x", "y", 23)
t1.intro()