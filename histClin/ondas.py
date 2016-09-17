frecuencia = int(input("Ingrese una frecuencia: "))
tipo_fre=  input("ingrese el tipo de frecuencia: ")

if frecuencia  > 30 and frecuencia <= 300 and tipo_fre == "KHZ":
    print("Baja Frecuencia (L/F) 30-300 kHz")

elif frecuencia > 300 and frecuencia <=3000:
    print("Media Frecuencia (M/F) kHz")
