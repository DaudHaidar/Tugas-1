Nilai_Ujian = int(input ("Nilai Teori : "))
Nilai_Praktek = int (input("Nilai Praktek: "))

if Nilai_Ujian >= 70 and Nilai_Praktek >= 70 :
    print("Selamat anda lulus! ")

elif Nilai_Ujian >= 70 and Nilai_Praktek < 70 :
    print("Anda harus mengulang ujian praktek")

elif Nilai_Ujian <70 and Nilai_Praktek >= 70 :
    print("Anda harus mengulang ujian teori")

elif Nilai_Ujian <70 and Nilai_Praktek <70 :
    print("Anda harus mengulang ujian teori dan praktek")