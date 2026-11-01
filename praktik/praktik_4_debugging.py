
# Praktik 4: Investigasi dan Perbaikan Bug
# Pertemuan 13 - Debugging dan Testing

# Fungsi menghitung rata-rata
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


# Fungsi menentukan status kelulusan
def status(nilai):
    if nilai >= 60:
        return "Lulus"

    return "Tidak lulus"


# Fungsi mencari nilai tertinggi
def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


# Data utama
nilai = [80, 60, 90, 70]


# Menampilkan hasil program
print("=== HASIL PROGRAM ===")

print("Data nilai:", nilai)
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Pengujian test case
print("\n=== PENGUJIAN TEST CASE ===")

test_case = [
    ("T1", "Rata-rata", [80, 60, 90, 70], 75.0),
    ("T2", "Rata-rata", [100, 80], 90.0),
    ("T3", "Status", 60, "Lulus"),
    ("T4", "Status", 59, "Tidak lulus"),
    ("T5", "Tertinggi", [80, 60, 90, 70], 90)
]

for id_test, jenis, input_data, expected in test_case:

    if jenis == "Rata-rata":
        actual = hitung_rata_rata(input_data)

    elif jenis == "Status":
        actual = status(input_data)

    elif jenis == "Tertinggi":
        actual = nilai_tertinggi(input_data)

    else:
        actual = None

    hasil = "PASS" if actual == expected else "FAIL"

    print(f"{id_test} | {jenis}")
    print("Expected:", expected)
    print("Actual:", actual)
    print("Status:", hasil)
    print("----------------------")


# Pengujian tambahan untuk data kosong
print("\n=== PENGUJIAN DATA KOSONG ===")

print("Rata-rata data kosong:", hitung_rata_rata([]))
print("Nilai tertinggi data kosong:", nilai_tertinggi([]))
