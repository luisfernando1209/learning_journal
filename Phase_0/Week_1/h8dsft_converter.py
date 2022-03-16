def CK ():
        pilihan = input("Ingin Cari Suhu apa (kelvin/celcius): ")
        if pilihan == 'kelvin':
            celcius = int(input("Tulis suhu dalam derajat celcius: "))
            kelvin = celcius + 273
            print(f"{celcius} derajat celcius sama dengan {kelvin} kelvin")
        elif pilihan == 'celcius':
            kelvin = int(input("Tulis suhu dalam kelvin: "))
            celcius = kelvin - 273
            print(f"{kelvin} kelvin sama dengan {celcius} derajat celcius")

def CKF ():
    pilihan = input("Sebutkan jenis suhu untuk diconvert ke fahrenheit(celcius/kelvin): ")
    if pilihan == "celcius":
        celcius = int(input("Tulis suhu dalam celcius: "))
        fahrenheit = (celcius*9/5) + 32
        print(f"{celcius} derajat celcius sama dengan {fahrenheit} derajat fahrenheit")
    elif pilihan == "kelvin":
        kelvin = int(input("Tulis suhu dalam kelvin: "))
        fahrenheit = ((kelvin-273)*9/5) + 32
        print(f"{kelvin} derajat celcius sama dengan {fahrenheit} derajat fahrenheit")

def FCK ():
    fahrenheit = int(input("Tulis suhu dalam fahrenheit: "))
    celcius = (fahrenheit-32) * 5/9
    kelvin = celcius + 273
    print(f"{fahrenheit} derajat fahrenheit sama dengan {celcius} derajat celcius, atau {kelvin} kelvin")

print('''
-------------------
Aplikasi Calculator
-------------------
Mau cari suhu apa ?
1. Suhu Kelvin <-> Celcius
2. Suhu Kelvin/Celcius -> Fahrenheit
3. Suhu Fahrenheit -> Kelvin/Celcius
4. Exit
''')
while True:
    pilih = int(input("Pilihan anda(1-3): "))


    if pilih == 1:
        CK()
    elif pilih == 2:
        CKF()
    elif pilih == 3:
        FCK()
    elif pilih == 4: 
        break