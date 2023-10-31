import random

modogrenici = input("Kolay mod için 'K' zor mod için 'Z' tuşuna basınız.\n")
oyunmodu = 0
if modogrenici == "Z":
    oyunmodu = 5
else:
    oyunmodu = 10

rastgele = random.randint(1,250)
sayac = 0
while 1:
    tahmin = int(input("1-250 arasında bir sayı giriniz\n"))
    if tahmin < 250 and tahmin > 1:
        if rastgele > tahmin:
            sayac += 1
            if sayac > oyunmodu:
                print(f"tahmin hakkın bitti GAME OVER\nRastgele seçilen sayı :{rastgele}")
                break
            else:
                print("Daha büyük bir sayı giriniz.\n")
        elif rastgele < tahmin:
            sayac += 1
            if sayac > oyunmodu:
                print(f"tahmin hakkın bitti GAME OVER\nRastgele seçilen sayı :{rastgele}")
                break
            else:
                print("Daha küçük bir sayı giriniz\n")
        else:
            print("Bravo doğru tahmin!!\n")
            tekraroyun = input("Tekrar Oynamak için 'R' tuşuna basınız\n")
            sayac = 0
            if tekraroyun == "R":
                rastgele = random.randint(1, 250)
                continue
            else:
                print("Bayyys")
                break
    else:
        print("Yanlış girdi.Tekrar deneyiniz.")
        continue

