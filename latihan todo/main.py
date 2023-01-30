import todo
def main():
    print("Aplikasi To-Do List")
    print("[1] Tambah Tugas")
    print("[2] Lihat Tugas")
    print("[3] Ubah Tugas")
    print("[4] Hapus Tugas")
    pilihan = int(input("Pilihan Anda: "))

    if pilihan == 1:
        name = input("Nama Tugas: ")
        todo.create_task(name)
    elif pilihan == 2:
        tasks = todo.read_tasks()
        for task in tasks:
            print(task[0], task[1], task[2])
    elif pilihan == 3:
        task_id = int(input("ID Tugas: "))
        name = input("Nama Tugas Baru: ")
        status = int(input("Status (0/1): "))
        todo.update_task(task_id, name, status)
    elif pilihan == 4:
        task_id = int(input("ID Tugas: "))
        todo.delete_task(task_id)
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
