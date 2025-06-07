#1

s_kitoblar = ["python cook book", "adventure of alice", "mobabook"]
print("Mening sevimli kitoblarim: ")
for kitob in s_kitoblar:
    print(kitob.title())

#2

print("5ta yoqtirgan filmlaringizni kiriting!")
film = []
for n in range(5):
    film.append(input(f"{n+1}- filmingizni kiriting: "))
print(
      f"Sizning birinchi va oxirgi kiritgan filmlaringiz: "
      f"{film[0].title()}, {film[4].title()}"
      )

#3

shaharlar = ["samarkand", "nawoi", "tokio", "kuala-lumpur"]
f_shahar = input("Shahar kiriting: ")
if f_shahar.lower() in shaharlar:
    print("Shahar mavjud")
else:
    print("Shahar topilmadi")

#4

raqamlar = [124534, 6423425, 6362454, 5362413, 6352254]#Istalgan raqamlar kiritish mumkin
raqamlar.reverse()
print(max(raqamlar))
print(min(raqamlar))

#5
mahsulotlar = []
for n in range(7):
    mahsulotlar.append(input(f"{n+1}-mahsulotingizni kiriting: "))
print(sorted(mahsulotlar))
print(sorted(mahsulotlar, reverse=True))

    
