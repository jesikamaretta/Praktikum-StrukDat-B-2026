# main.py

from tabulate import tabulate
from kurs import kurs
from konverter import konversi


def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])

    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))


def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


print("=== KONVERTER MATA UANG ===")
tampilkan_kurs()

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()

try:
    jumlah = float(input("Jumlah: "))
    hasil = konversi(jumlah, dari, ke)

    print()

    if dari == "IDR":
        print(f"{format_rupiah(jumlah)} = {hasil:.2f} {ke}")
    elif ke == "IDR":
        print(f"{jumlah} {dari} = {format_rupiah(hasil)}")
    else:
        print(f"{jumlah} {dari} = {hasil:.2f} {ke}")

except ValueError as e:
    print("Terjadi kesalahan:", e)