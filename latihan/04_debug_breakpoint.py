# Latihan 4: Debugging dengan Breakpoint

def hitung_nilai(nilai):
    total = 0

    for angka in nilai:
        total += angka

    rata_rata = total / len(nilai)

    return rata_rata


data_nilai = [80, 90, 70, 85]

hasil = hitung_nilai(data_nilai)

print("Data nilai:", data_nilai)
print("Rata-rata nilai:", hasil)