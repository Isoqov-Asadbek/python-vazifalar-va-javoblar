#Nested dictionaries uchun savollarga javoblar
#1-mashq

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro'
            }

qodiriy = {'ism':'Abdulla Qodiriy',
            'tyil':1894,
            'vyil':1938,
            'tjoy':'Toshkent'
            }

vohidov = {'ism':'Erkin Vohidov',
            'tyil':1936,
            'vyil':2016,
            'tjoy':"Farg'ona"
            }

navoiy = {'ism':'Alisher Navoiy',
            'tyil':1441,
            'vyil':1501,
            'tjoy':"Xirot"
            }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for shaxs in shaxslar:
    ism = shaxs["ism"]
    tyil = shaxs["tyil"]
    vyil = shaxs["vyil"]
    tjoy = shaxs["tjoy"]
    print(f"{ism.title()} {tyil}-yilda {tjoy.title()}da tug'ilgan."
          f"U {vyil-tyil} yil umr ko'rgan va {vyil}-yilda vafot etgan\n"
          )

#2-mashq

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for ism, kino in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari: ")
    for s_kino in kino:
        print(s_kino.title())

#3-mashq

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
    "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
    "aqsh":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
    }
for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()

    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
      f"\nHududi: {info['maydon']:_} kv.km"#biror sonli variabledan so'ng
      f"\nAholisi: {info['aholi']:_}"#:_ yoki :, ishlatsak o'sha variabledani
      f"\nPul birligi: {info['pul birligi'].title()}")#sonlarni avtomatik yaxlitlab beradi.