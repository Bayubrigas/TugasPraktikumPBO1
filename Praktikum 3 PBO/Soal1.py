import math

class Kalkulator:
  def __init__(self, nilai):
    self.nilai = nilai

  def __add__(self, other):
    return Kalkulator(self.nilai + other.nilai)

  def __sub__(self, other):
    return Kalkulator(self.nilai - other.nilai)

  def __mul__(self, other):
    return Kalkulator(self.nilai * other.nilai)

  def __truediv__(self, other):
    if other.nilai == 0:
      raise ValueError("Tidak bisa membagi dengan nol")
    return Kalkulator(self.nilai / other.nilai)

  def __pow__(self, other):
    return Kalkulator(self.nilai ** other.nilai)

  def log(self):
    if self.nilai <= 0:
      raise ValueError("Logaritma hanya bisa dihitung untuk nilai positif")
    return math.log(self.nilai)

  def __str__(self):
    return str(self.nilai)

a = Kalkulator(10)
b = Kalkulator(5)

print("a + b =", (a + b))
print("a - b =", (a - b))
print("a * b =", (a * b))
print("a / b =", (a / b))
print("a ^ b =", (a ** b))
print("log(a) =", a.log())