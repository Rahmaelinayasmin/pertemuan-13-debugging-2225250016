# Kasus 3: Bug File Nilai

nama_file = "nilai.txt"

try:
    with open(nama_file, "r") as file:
        data = file.read()

        if data.strip() == "":
            print("File kosong.")
        else:
            nilai = [int(x) for x in data.split()]
            print("Data nilai:", nilai)

except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")

except ValueError:
    print("File berisi data yang tidak valid.")