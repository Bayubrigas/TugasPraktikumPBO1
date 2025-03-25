class Todolist:
  def __init__(self):
    self.__tasks = []

  def add_task(self, task):
    if not task.strip():
      raise ValueError("Tugas tidak boleh kosong")
    self.__tasks.append(task)
    print(f"Tugas {task} berhasil ditambahkan")

  def remove_task(self, task):
    if task not in self.__tasks:
      raise ValueError("Tugas tidak ditemukan")
    self.__tasks.remove(task)
    print(f"Tugas {task} berhasil dihapus")

  def display_tasks(self):
    if not self.__tasks:
      print("Tidak ada daftar tugas")
    else:
      print("Daftar tugas:")
      for i, task in enumerate(self.__tasks, start=1):
        print(f"{i}. {task}")

def main():
  list_tugas = Todolist()
  try:
    while True:
      print("1. Tambah tugas")
      print("2. Hapus tugas")
      print("3. Lihat daftar tugas")
      print("4. Keluar")
      pilihan = int(input("Masukkan pilihan: "))

      if pilihan == 1:
        tugas = input("Masukkan tugas: ")
        list_tugas.add_task(tugas)
      elif pilihan == 2:
        tugas = input("Masukkan tugas: ")
        list_tugas.remove_task(tugas)
      elif pilihan == 3:
        list_tugas.display_tasks()
      elif pilihan == 4:
        break
      else:
        raise ValueError("Pilihan tidak valid")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()