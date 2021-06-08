# Basic calculator in python 3.6
# Made in Turkey
# By akerem16

# [EN] First we will get number of operations. We will run the code block according to what action will be taken.
# [TR] ilk önce işlem numarasını almamız gerekiyor. Hangi işlem yapılacaksa ona göre kod bloğu çalıştıracağız.
operationnumber = str(input("""
[EN]
Hello i am a basic calculator!
Thanks to me, you can quickly do the following:
1- Addition (+)
2- Subtraction (-)
3- Multiplication (*)
4- Division (/)
5- Get power (^^)
0- Exit code

[TR]
Merhaba. Ben basit bir hesap makinesiyim!
Benim sayemde aşağıdakileri işlemleri hızlıca yapabilirsiniz:
1- Toplama (+)
2- Çıkarma (-)
3- Çarpma (*)
4- Bölme (/)
5- Üssünü alma (^^)
0- Çıkış

Your choice: """))


# [EN] Now we define operations according to the selection made.
# [TR] Şimdi yapılan seçime göre işlemleri tanımlıyoruz.
if operationnumber == "1":
    print("Result:", int(input("Number 1: ")) + int(input("Number 2: ")))
elif operationnumber == "2":
    print("Result:", int(input("Number 1: ")) - int(input("Number 2: ")))
elif operationnumber == "3":
    print("Result:", int(input("Number 1: ")) * int(input("Number 2: ")))
elif operationnumber == "4":
    print("Result:", int(input("Number 1: ")) / int(input("Number 2: ")))
elif operationnumber == "5":
    print("Result:", int(input("Number 1: ")) ** int(input("Number 2: ")))
elif operationnumber == "0":
    exit()
else:
    print("[EN] Wrong choice entered.")
    print("[TR] Hatalı giriş yapıldı.")
    exit()