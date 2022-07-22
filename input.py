import time


print("assalomu aleykum!saytimizga xush kelipsiz")
time.sleep(4.2)

b = input("Siz saytimizdan hisob ochgansiz.")

login = input("Loginingizni kiriting: ")

time.sleep(3)
pas = int(input("Parolingizni kiriting: "))

if login == 'Shaxzod' and pas == 12345678:
    print(f"Xush kelipsiz, {login} !")
elif login ==  'python' and pas == 1:
    print(f"Xush kelipsiz, {login} !")
else:
    print("Siz login va parolingizni noto'g'ri kiritdingiz")