print("""
*****************************
*                           *
*                           *
*  yüzde hesaplama programı *
*                           *
*                           *
*****************************
""")
while True:
    birinci_sayi = int(input("yüzdesi alınacak sayıyı girin : "))
    ikinci_sayi = int(input("{} sayısının yüzde kaçını istiyorsunuz : ".format(birinci_sayi)))
    yuzde = birinci_sayi * ikinci_sayi / 100
    print("yüzde {}".format(yuzde))
    secim = input("toplama veya çıkarma için seçim yapın [+][-]")
    if secim == "+":
        sonuc = birinci_sayi + yuzde
        print("{} + {} = {}".format(birinci_sayi,yuzde,sonuc))
    elif secim == "-":
        sonuc = birinci_sayi - yuzde
        print("{} - {} = {}".format(birinci_sayi,yuzde,sonuc))
    else:
        print("toplama veya çıkarma işlemi iptal edildi")
