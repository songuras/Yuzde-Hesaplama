def artma(x, y):
    artis = y - x
    artis = artis / x
    artis = artis * 100
    return artis


def azalma(x, y):
    azalis = y - x
    azalis = azalis / x
    azalis = azalis * 100
    return azalis


def yuzde(x, y):
    yuzde = x * y / 100
    return yuzde


while True:
    print("yüzde hesaplama için 1 artma için 2 azalma için 3 : ")
    menu = input()
    if menu == "1":
        yuzdesi_alinacak_sayi = float(input("yüzdesi alinacak sayi : "))
        yuzde_kac = float(input("{} sayisinin yuzde kacini istiyorsunuz : ".format(yuzdesi_alinacak_sayi)))
        print(yuzde(yuzdesi_alinacak_sayi, yuzde_kac))
    elif menu == "2":
        ilk = float(input("ilk miktar : "))
        son = float(input("son miktar : "))
        print("artış = %",artma(ilk,son))
    elif menu == "3":
        ilk = float(input("ilk miktar : "))
        son = float(input("son miktar : "))
        print("azalış = %",azalma(ilk, son))
    else:
        print("geçersiz işlem . . .")