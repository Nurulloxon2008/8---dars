Books = {}

def Addbook(nomi, **kwargs):
    Books[nomi] = kwargs
    return "Kitob qo'shildi"

def sellbook(nomi):
    if nomi in Books and Books[nomi]['Quantity'] > 0:
        Books[nomi]['Quantity'] -= 1
        print(f"{nomi} kitobi sotildi. Qolgan soni: {Books[nomi]['Quantity']}")
    else:
        print(f"{nomi} kitobi mavjud emas yoki tugagan!")

while True:
    search = input("Kitob nomini kiriting >>> ")
    if search in Books:
        print(f"Malumotlari: {Books[search]}")
        savol = input(f"{search} kitobini sotib olishni xohlaysizmi? (ha/yo'q) ")
        if savol == "ha":
            sellbook(search)
            if Books[search]['Quantity'] == 0:
                del Books[search]
    else:
        savol = input(f"{search} kitobi topilmadi. Boshqa kitob qo'shasizmi? (ha/yo'q) ")
        if savol == "ha":
            Author = input("Muallifini kiriting: ")
            Price = input("Narxini kiriting: ")
            Quantity = int(input("Soni kiriting: "))
            print(Addbook(search, Author=Author, Price=Price, Quantity=Quantity))        