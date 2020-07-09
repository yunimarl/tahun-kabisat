tahun = int(input())
if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print ("Kabisat")
        else:
            print ("Tidak habis dibagi 400 jadi Bukan Tahun Kabisat")
    else:
        print ("Kabisat")
else:
    print ("Bukan Tahun Kabisat")
