import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
gir = int(input("Parola uzunluğu giriniz."))
sifre =""
for i in range(gir):
    sifre += random.choice(karakterler)
print(sifre)