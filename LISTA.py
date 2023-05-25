# SKRYPT 1 LICZBY

print("Cześć, podaj dwie liczby całkowite a wykonam na nich kilka działań matematycznych!")
def calculator_addition(number1,number2):
    return number1+number2
def calculator_difference(number1,number2):
    return number1-number2
def calculator_multiplication(number1,number2):
    return number1*number2
def calculator_division(number1,number2):
    if number2==0:
        return None
    else:
        return number1/number2
def calculator_element(number1,number2):
    if number1<=0 and number2<=0:
        return None, None
    elif number1<=0 and number2>0:
        return None, number2**0.5
    elif number1>0 and number2<=0:
        return number1**0.5, None
    else:
        return number1**0.5, number2**0.5
try:
    number1=int(input("Podaj pierwszą liczbę: "))
    number2=int(input("Podaj drugą liczbę: "))
    print("Suma wynosi:",calculator_addition(number1,number2))
    print("Różnica wynosi:",calculator_difference(number1,number2))
    print("Iloczyn wynosi:",calculator_multiplication(number1,number2))
    print("Dzielenie wynosi:",calculator_division(number1,number2))
    print("Pierwiastkowanie:",calculator_element(number1,number2))
except:
    print("Przepraszam, nie jestem w stanie tego wykonać!")


# SKRYPT 2 BRYŁY

Pi=3.14
def care(radius):
    square= 4*Pi*radius**2
    volume= 4/3*Pi*radius**3
    return square,volume
def cone(radius, height):
    slantheight=(radius**2+height**2)**0.5
    square=Pi*radius*slantheight+Pi*radius**2
    volume=1/3*Pi*radius**2*height
    return square,volume
def cube(side):
    square=6*side**2
    volume=side**3
    return square, volume
while True:
    print("Wybierz bryłę:")
    print("1 - Kula")
    print("2 - Stożek")
    print("3 - Sześcian")
    print("4 - Wyjdź ze skryptu")
    choice=input("Wybieram: ")

    if choice=="1":
        radius=float(input("Podaj promień: "))
        square, volume=care(radius)
        print("Pole kuli wynosi: ", square, "a objętość: ", volume)
    elif choice=="2":
        radius=float(input("Podaj promień: "))
        height=float(input("Podaj wysokość: "))
        square, volume=cone(radius,height)
        print("Pole stożka wynosi: ", square, "a objętość: ", volume)
    elif choice=="3":
        side=float(input("Podaj długość boku: "))
        square, volume=cube(side)
        print("Pole sześcianu wynosi: ", square, "a objętość: ", volume)
    elif choice=="4":
        print("Dzięki, narazie.")
        break
    else:
        print("Coś poszło nie tak. Spróbuj ponownie!")

# SKRYPT 3 PRZELICZNIK

def count_height(feet):
    meters= feet*0.3048
    centimeters= meters*100
    milimeters= centimeters*10
    kilometers= meters/1000
    return meters, centimeters, milimeters, kilometers

try:
    feet = float(input("Wpisz wysokość w stopach: "))
    if feet>0:
        print("Twoja wysokość w różnych jednostkach.")
        print("W metrach: ", count_height(feet)[0])
        print("W centymetrach: ", count_height(feet)[1])
        print("W milimetrach: ", count_height(feet)[2])
        print("W kilometrach: ", count_height(feet)[3])
    elif feet<=0:
        print("Ujemna wysokość? Hmmm...")
    else:
        print("Nie potrafię tego obliczyć.")
except:
    print("Coś poszło nie tak..")


# SKRYPT 4 WYSOKOŚĆ LOTU

safety_height = 5000
try:
    height = int(input("Na jakiej wysokości lecimy? (podaj w metrach): "))
    if height < safety_height and height > 0:
        print(height / 1000, "km to za nisko!")
    elif height >=5000:
        print("Na tej wysokości jesteś już bezpieczny.")
    elif height <= 0:
        print("To chyba niemożliwe..")
    else:
        print("Nie potrafię tego obliczyć.")
except:
    print("Zła wartość!")

# SKRYPT 5 BMI
# TUTAJ DAŁEM ZAOKGRĄGLENIA I POMNOŻYŁEM PRZEZ 10000 ŻEBY WYCHODZIŁY ODPOWIEDNIE LICZBY, CHOCIAŻ NIE WIEM CZY TAK MIAŁO BYĆ.

def BMI(mass, height):
    bmi = (mass / (height * height))*10000

    if bmi <= 18.5:
        print("Masz niedowagę :(")
    elif bmi <= 24.99:
        print("Twoja waga jest prawidłowa :)")
    else:
        print("Masz nadwagę!!!")

    return bmi

print("Witaj w kalkulatorze BMI!")
try:
    mass = float(input("Podaj swoją wagę w kg: "))
    height = float(input("Podaj swój wzrost w m: "))
    bmi = BMI(mass, height)
    print("Twoje BMI wynosi:", round(bmi, 2))
except:
    print("Podałeś złe wartości!")

# SKRYPT 6
# OD TEGO MOMENTU JUŻ NIE DAWAŁEM INPUT I EXCEPT, NIE DO KOŃCA WIEDZIAŁEM CZY TE SKRYPTY MAJĄ WYGLĄDAĆ
# TAK JAK WYŻEJ CZY RACZEJ WŁAŚNIE TAK PROSTO JAK PONIŻEJ, MÓGŁBY PAN DAĆ ZNAĆ :)
def convert(number, kind):
    if kind == "binary":
        dec = int(number)
        return f"Binary: {dec}", f"Hexadecimal: {hex(dec)}", f"Octal: {oct(dec)}"
    elif kind == "hexadecimal":
        dec = int(number, 16)
        return f"Decimal: {dec}", f"Binary: {bin(dec)}", f"Octal: {oct(dec)}"
    elif kind == "octal":
        dec = int(number, 8)
        return f"Decimal: {dec}", f"Binary: {bin(dec)}", f"Hexadecimal: {hex(dec)}"
    else:
        dec = int(number)
        return f"Decimal: {dec}", f"Binary: {bin(dec)}", f"Hexadecimal: {hex(dec)}", f"Octal: {oct(dec)}"

print(*convert(987, "decimal"))
print(*convert("3C", "hexadecimal"))
print(*convert("11110011", "binary"))


# SKRYPT 7

def dec_rom(number):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_number = ""
    i = 0
    while number > 0:
        for _ in range(number // value[i]):
            rom_number += symbol[i]
            number -= value[i]
        i += 1
    return rom_number

def rom_dec(rom_number):
    rom_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    dec_number = 0
    i = 0
    while i < len(rom_number):
        if i+1 < len(rom_number) and rom_dict[rom_number[i]] < rom_dict[rom_number[i+1]]:
            dec_number += rom_dict[rom_number[i+1]] - rom_dict[rom_number[i]]
            i += 2
        else:
            dec_number += rom_dict[rom_number[i]]
            i += 1
    return dec_number

print(dec_rom(369))
print(dec_rom(73))
print(dec_rom(2137))

print(rom_dec("MMXXI"))
print(rom_dec("LVIII"))
print(rom_dec("MCMXCIV"))