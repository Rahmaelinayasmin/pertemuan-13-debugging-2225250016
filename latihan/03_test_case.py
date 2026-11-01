# Latihan 3: Test Case Bug Batas Kelulusan

def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Test case
test_case = [59, 60, 61]

for nilai in test_case:
    hasil = status_lulus(nilai)
    print(f"Nilai: {nilai} | Status: {hasil}")