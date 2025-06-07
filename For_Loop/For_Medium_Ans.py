# #1-mashq

# #1-usuli.Matematik Formuladan Foydalanib ortiqcha yozuvlarsiz
# n = int(input("Istalgan sonni kiriting: "))
# print(f"{n}ning umumiy yig'indisi: {n*(n+1)//2}")

# #2-usuli for sikli bilan
# yigindi = 0
# son = int(input("Istalgan sonni kiriting: "))
# for n in range(1, son + 1):
#     yigindi += son
# print("Yig'indi:", yigindi)




# #2-mashq
# musbat_sanogi = 0
# for i in range(10):
#     son = int(input(f"{i+1}-sonni kiriting: "))
#     if son > 0:
#         musbat_sanogi += 1
# print("Musbat sonlar soni:", musbat_sanogi)

# #3-mashq


# matn = input("Matn kiriting: ")
# katta_harf = 0
# for belgi in matn:
#     if belgi.isupper():
#         katta_harf += 1
# print(f"Katta harflar soni: {katta_harf}")

# #4-mashq

# sonlar = list(range(1,21))
# for son in sonlar:
#     if son % 3 == 0:
#         print(son)

# #5-mashq
# matn = input("Matn kiriting: ").lower()
# unlilar = "aeiou"
# topilgan_unlilar = []

# for harf in matn:
#     if harf in unlilar and harf not in topilgan_unlilar:
#         topilgan_unlilar.append(harf)

# print(f"Takrorsiz unlilar: {', '.join(topilgan_unlilar)}")