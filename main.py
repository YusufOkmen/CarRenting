tumAraclar = []

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

# Objects
arac1 = Araclar("Volvo", "Volvo XC90", 5000, "Kullanilabilir", "-")

arac2 = Araclar("BMW", "BMW i8", 6000, "Kullanilamaz", "3 hafta sonra")

arac3 = Araclar("Volvo", "XC40", 3000, "Kullanilamaz", "Bir kac gun sonra")

arac4 = Araclar("Volvo", "Volvo XC60", 4500, "Kullanilabilir", "-")

arac5 = Araclar("Audi", "Audi A3", 2000, "Kullanilamaz", "1 gun sonra")

arac6 = Araclar("Audi" ,"Audi A6", 6000, "Kullanilabilir", "-")

arac7 = Araclar("Renault", "Renault Clio 1.2", 500, "Kullanilabilir", "-")

arac8 = Araclar("Renault", "Megan", 1000, "Kullanilamaz", "2 gun sonra")

arac9 = Araclar("BMW", "BMW i5", 4500, "Kullanilabilir", "-")

arac10 = Araclar("Bugatti", "Bugatti Chiron 8.0", 15000, "Kullanilabilir", "-")


