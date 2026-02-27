from kurs import kurs


def konversi(jumlah, dari, ke):
    dari = dari.upper()
    ke = ke.upper()

    # Jika dari IDR ke mata uang lain
    if dari == "IDR" and ke in kurs:
        return jumlah / kurs[ke]

    # Jika dari mata uang lain ke IDR
    elif ke == "IDR" and dari in kurs:
        return jumlah * kurs[dari]

    # Jika dari mata uang asing ke mata uang asing lain
    elif dari in kurs and ke in kurs:
        jumlah_idr = jumlah * kurs[dari]
        return jumlah_idr / kurs[ke]

    # Jika IDR ke IDR
    elif dari == "IDR" and ke == "IDR":
        return jumlah

    else:
        raise ValueError("Kode mata uang tidak valid.")