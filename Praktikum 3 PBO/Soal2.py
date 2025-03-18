import random

class Father:
  def __init__(self, blood_types):
    self.blood_types = blood_types

class Mother:
  def __init__(self, blood_types):
    self.blood_types = blood_types

class Child:
  def __init__(self, father, mother):
    self.father_blood_type = random.choice(father.blood_types)
    self.mother_blood_type = random.choice(mother.blood_types)
    self.blood_type = self.determine_blood_type()

  def determine_blood_type(self):
    possible_blood_types = {
      ('A', 'A'): 'A',
      ('A', 'O'): 'A',
      ('O', 'A'): 'A',
      ('B', 'B'): 'B',
      ('B', 'O'): 'B',
      ('O', 'B'): 'B',
      ('A', 'B'): 'AB',
      ('B', 'A'): 'AB',
      ('O', 'O'): 'O'
    }
    return possible_blood_types.get((self.father_blood_type, self.mother_blood_type), 'Tidak Diketahui')

father_blood_types = input("Masukkan golongan darah ayah: ")
mother_blood_types = input("Masukkan golongan darah ibu: ")

father = Father(father_blood_types)
mother = Mother(mother_blood_types)
child = Child(father, mother)

print(f"Golongan darah anak: {child.blood_type}")