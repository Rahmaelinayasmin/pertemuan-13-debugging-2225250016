
# PERTEMUAN 13 - DEBUGGING, TRACING, TESTING, DAN TEST CASE

## Identitas Mahasiswa

Nama  : (Rahma Elina Yasmin)
NIM   : (2225250016)
Kelas : (3F)

## Tujuan

Tujuan praktikum ini adalah menguji program secara sistematis,
menelusuri aliran eksekusi, menggunakan debugger VS Code,
merancang test case, mengidentifikasi penyebab bug, dan
memperbaiki program.

Adapun tujuan khususnya:
1. Membedakan syntax error, runtime error, dan logical error.
2. Melakukan tracing nilai variabel.
3. Menggunakan breakpoint pada VS Code.
4. Membaca traceback.
5. Menyusun test case normal, batas, kosong, dan tidak valid.
6. Membandingkan expected result dengan actual result.
7. Mengidentifikasi dan memperbaiki bug.
8. Melakukan pengujian ulang setelah perbaikan.

## Kasus

Praktikum ini menggunakan program pengolahan nilai mahasiswa.
Program awal memiliki tiga bug utama, yaitu:

1. Perhitungan rata-rata menggunakan pembagi tetap 5.
2. Status kelulusan menggunakan operator > sehingga nilai 60
   dianggap tidak lulus.
3. Pencarian nilai tertinggi menggunakan operator < sehingga
   hasil yang diperoleh tidak tepat.

## Cara Menjalankan

1. Buka folder project melalui Visual Studio Code.
2. Pastikan Python 3 sudah terinstal.
3. Buka Terminal pada VS Code.
4. Jalankan file latihan dengan perintah:

    python latihan/01_trace_loop.py

    python latihan/02_trace_fungsi.py

    python latihan/03_test_case.py

    python latihan/04_debug_breakpoint.py

5. Jalankan program praktik dengan perintah:

    python praktik/praktik_4_debugging.py

## Tabel Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|----|-------|----------|-------------|-------------|
| T1 | [80,60,90,70] | 75.0 | 60.0 | FAIL |
| T2 | [100,80] | 90.0 | 36.0 | FAIL |
| T3 | Nilai 60 | Lulus | Tidak lulus | FAIL |
| T4 | Nilai 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80,60,90,70] | 90 | 0 | FAIL |

## Bug Report

### Bug 1 - Perhitungan Rata-rata

Gejala:
Hasil rata-rata tidak sesuai dengan jumlah data.

Akar penyebab:
Program menggunakan pembagi tetap 5.

Perbaikan:
Mengganti pembagi dengan len(nilai) dan menambahkan
penanganan data kosong.

### Bug 2 - Status Kelulusan

Gejala:
Nilai 60 dianggap tidak lulus.

Akar penyebab:
Program menggunakan operator > 60.

Perbaikan:
Mengubah operator menjadi >= 60.

### Bug 3 - Nilai Tertinggi

Gejala:
Program tidak menghasilkan nilai tertinggi dengan benar.

Akar penyebab:
Program menggunakan operator < untuk membandingkan
nilai dan menginisialisasi nilai tertinggi dengan 0.

Perbaikan:
Menggunakan nilai pertama sebagai nilai awal dan
operator > untuk mencari nilai tertinggi.

## Hasil Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|----|----------|--------------------------|--------|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

Seluruh lima test case berhasil setelah program diperbaiki.

## Refleksi

Teknik debugging yang paling membantu adalah tracing
dan penggunaan breakpoint karena dapat menunjukkan
perubahan nilai variabel pada setiap langkah program.

Saya memahami bahwa kesalahan program tidak selalu
berupa syntax error atau runtime error. Logical error
juga perlu diperiksa melalui test case yang sesuai.

Setelah memperbaiki bug, program harus diuji kembali
untuk memastikan hasilnya benar dan tidak menimbulkan
kesalahan baru.

## Kesimpulan

Debugging dan testing merupakan proses penting dalam
pembuatan program. Melalui praktikum ini, saya belajar
mengidentifikasi bug, menemukan akar penyebab,
memperbaiki kode, dan melakukan retest menggunakan
test case yang telah dirancang.
