tumAraclar = []
kullanilabilirAraclarList = []

volvo = []
bmw = []
renault = []
audi = []
bugatti = []

# Class
class Araclar:
    def __init__(self, aracMarka, aracModel, gunlukFiyat, kiraDurum, tahminiKira):
        self.marka = aracMarka
        self.model = aracModel
        self.fiyat = gunlukFiyat
        self.kira = kiraDurum
        self.tahmin = tahminiKira
        tumAraclar.append(self.model)
        
        if self.marka == "Volvo":
            volvo.append(self.model)

        if self.marka == "BMW":
            bmw.append(self.model)

        if self.marka == "Renault":
            renault.append(self.model)

        if self.marka == "Audi":
            audi.append(self.model)

        if self.marka == "Bugatti":
            bugatti.append(self.model)

        if self.kira == "Kullanilabilir":
            kullanilabilirAraclarList.append(self.model)

# Objects
arac1 = Araclar("Volvo", "Volvo XC90", 5000, "Kullanilabilir", "-")

arac2 = Araclar("BMW", "BMW i8", 6000, "Kullanilamaz", "3 hafta sonra")

arac3 = Araclar("Volvo", "Volvo XC40", 3000, "Kullanilamaz", "Bir kac gun sonra")

arac4 = Araclar("Volvo", "Volvo XC60", 4500, "Kullanilabilir", "-")

arac5 = Araclar("Audi", "Audi A3", 2000, "Kullanilamaz", "1 gun sonra")

arac6 = Araclar("Audi" ,"Audi A6", 6000, "Kullanilabilir", "-")

arac7 = Araclar("Renault", "Renault Clio 1.2", 500, "Kullanilabilir", "-")

arac8 = Araclar("Renault", "Renault Megan", 1000, "Kullanilamaz", "2 gun sonra")

arac9 = Araclar("BMW", "BMW i5", 4500, "Kullanilabilir", "-")

arac10 = Araclar("Bugatti", "Bugatti Chiron 8.0", 15000, "Kullanilabilir", "-")

aracListe = [arac1, arac2, arac3, arac4, arac5, arac6, arac7, arac8, arac9, arac10]

# Functions
def main():
    while True:
        print("\b")
        print("     ARAÇ KİRALAMA UYGULAMASI")
        print("\b")
        print("PANEL \n 1-Araç Kirala \n 2-Tüm Araçları Göster \n 3-Kullanılabilir Araçları Göster \n 4-Uygulamadan Çık")
        print("\b")
        karar = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz."))
        print("\b")

        if karar == 1:
            aracKiralama()
        elif karar == 2:
            genelAraclar()
        elif karar == 3:
            kullanilabilirAraclar()
        elif karar == 4:
            break

def aracKiralama():
    gir = input("Lütfen aratmak istediğiniz aracın markasını giriniz: ")
    
    if gir == "Volvo":
        print(volvo)
        gir2 = input("Lütfen listelenen modellerden birini giriniz: ")
        for arac in aracListe:
            if gir2 == arac.model:
                print(f"Aradığınız araç blundu")
                print(f"Araç: {arac.model}, aracın günlük fiyatı: {arac.fiyat}, aracin kiralanabilirlik durumu: {arac.kira}")
                if arac.kira == "kullanilamaz":
                    print(f"Aracın tahmini olarak kullanıma açılma süresi: {arac.tahmin}")
    elif gir == "BMW":
        print(bmw)
        gir2 = input("Lütfen listelenen modellerden birini giriniz: ")
        for arac in aracListe:
            if gir2 == arac.model:
                print(f"Aradığınız araç blundu")
                print(f"Araç: {arac.model}, aracın günlük fiyatı: {arac.fiyat}, aracin kiralanabilirlik durumu: {arac.kira}")
                if arac.kira == "Kullanilamaz":
                    print(f"Aracın tahmini olarak kullanıma açılma süresi: {arac.tahmin}")
    elif gir == "Audi":
        print(audi)
        gir2 = input("Lütfen listelenen modellerden birini giriniz: ")
        for arac in aracListe:
            if gir2 == arac.model:
                print(f"Aradığınız araç blundu")
                print(f"Araç: {arac.model}, aracın günlük fiyatı: {arac.fiyat}, aracin kiralanabilirlik durumu: {arac.kira}")
                if arac.kira == "Kullanilamaz":
                    print(f"Aracın tahmini olarak kullanıma açılma süresi: {arac.tahmin}")
    elif gir == "Renault":
        print(renault)
        gir2 = input("Lütfen listelenen modellerden birini giriniz: ")
        for arac in aracListe:
            if gir2 == arac.model:
                print(f"Aradığınız araç blundu")
                print(f"Araç: {arac.model}, aracın günlük fiyatı: {arac.fiyat}, aracin kiralanabilirlik durumu: {arac.kira}")
                if arac.kira == "Kullanilamaz":
                    print(f"Aracın tahmini olarak kullanıma açılma süresi: {arac.tahmin}")
    elif gir == "Bugatti":
        print(bugatti)
        gir2 = input("Lütfen listelenen modellerden birini giriniz: ")
        for arac in aracListe:
            if gir2 == arac.model:
                print(f"Aradığınız araç blundu")
                print(f"Araç: {arac.model}, aracın günlük fiyatı: {arac.fiyat}, aracin kiralanabilirlik durumu: {arac.kira}")
                if arac.kira == "Kullanilamaz":
                    print(f"Aracın tahmini olarak kullanıma açılma süresi: {arac.tahmin}")

def genelAraclar():
    tumAraclar.sort()
    for i in tumAraclar:
        print(i)

def kullanilabilirAraclar():
    print("Kullanılabilir Araçlarımız:")
    for arac in kullanilabilirAraclarList:
        print(arac)

main()