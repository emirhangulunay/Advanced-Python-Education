from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Movie:
    title: str
    director: str
    year: int         
    duration: int

    def __repr__(self):
        return (
            f"Movie(title={self.title!r}, "
            f"director={self.director!r}, "
            f"year={self.year!r}, "
            f"duration={self.duration} dk)"
        )    
    def __str__(self):
        return f"{self.title} ({self.year}) - Director: {self.director}, year = {self.year!r}, duration = {self.duration} dakika"
    
    def __len__(self):
        return self.duration
    

    def __del__(self):
        print(f"Deleted movie: {self.title}")

    
    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return(self.title, self.director, self.year) == (other.title, other.director, other.year)
    

    def __lt__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.year < other.year
    
    def __add__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        
        return self.duration + other.duration
    

    def __bool__(self):
        return self.duration > 0
    

m1 = Movie("Mr. Robot", "Sam Esmail", 2024, 120)
m2 = Movie("Matrix", "Başka Yönetmen", 2020, 90)
m3 = Movie("Fight Club", "David Fincher", 2024, 120)


print("repr(m1):", repr(m1))

print("str(m1):", str(m1))
print("print(m1):", m1)

print("m1 uzunluğu(len):", len(m1), "dakika")

print("m1 == m3 ?", m1 == m3)
print("m1 == m2 ?", m1 == m2)

print("m2 < m1 ?", m1 > m2)

filmler = [m1, m2, m3]
sirali_filmler = sorted(filmler)

print("\nSıralı filmler (yıla göre):")

for f in sirali_filmler:
    print(f)

toplam_sure = m1 + m2
print("\nToplam süre (m1 + m2):", toplam_sure, "dakika")

if m1:
    print("\nm1 True sayıldı (süresi 0'dan büyük).")


del m2