import math

def calculator():
  try:
    numbers = float(input("Masukkan angka yang ingin di kuadratkan: "))
    
    if numbers <= 0:
      print("Akar kuadrat dari 0 atau bilangan negatif tidak diperbolehkan")
    else:
      result = math.sqrt(numbers)
      print(f"Akar kuadrat dari {numbers} adalah {result}")

  except ValueError:
    print("Input yang diterima harus berupa angka. Silahkan coba lagi")

if __name__ == "__main__":
  calculator()