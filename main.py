#1
a=int(input("Birinci ededi daxil et:"))
b=int(input("Ikinci ededi daxil et:"))
if (a>b):
    print(a)
else:
        print(b)
#2 
a=int(input())
b=int(input())
c=int(input())
print((a+b+c)/3)
#3
a=int(input("Ededi daxil et:"))
if a<0:
   print("Menfi")
elif a==0:
   print("Sifir")
else: 
   print("Musbet")
#4
a=int(input("Ayi daxil et:"))
if (a==1 or a==2 or a==12):
   print("Qis")
elif (a==3 or a==4 or a==5):
    print("Yay")
elif(a==6 or a==7 or a==8):
    print("Yaz")
else:
    print("Payiz")
#5
a = int(input("Yaşını daxil et: "))
if a >= 18:
    b = input("Sürücülük vəsiqən varmı? (Bəli/Xeyr): ")
    if b == "Bəli":
        print("Maşın sürə bilərsən")
    else:
        print("Vəsiqə lazım")
else:
    print("Yaş çatmır")