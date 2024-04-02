#Kalkulator Kalkulator jumlah bil elektrik
print('Kalkulator jumlah bil elektrik')

#Input penggunaan elektrik
penggunaan_elektrik=float(input("Masukkan penggunaan elektrik(kWj):"))

#Proses mengira jumlah bil elektrik
if penggunaan_elektrik <=200:
    bayaran = penggunaan_elektrik * 0.218
elif penggunaan_elektrik <= 300:
    bayaran = (200*0.218)+((penggunaan_elektrik-200)*0.334)
elif penggunaan_elektrik <= 600:
    bayaran = (200*0.218) +(100 * 0.334) + (penggunaan_elektrik-300)*0.516
elif penggunaan_elektrik <= 900:
    bayaran = (200*0.218) +(100 * 0.334) + (300*0.516) + ((penggunaan_elektrik-600)*0.546)

#Output
print("Jumlah bil elektrik yang perlu anda bayar ialah RM",round(bayaran,2))
