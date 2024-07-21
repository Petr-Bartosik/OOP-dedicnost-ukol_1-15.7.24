#musel jsem nastudovat neco o lodich, ale v testu jsem nechal nahodna cisla
#neustale mi to hazelo chybu, tak jsem to provetral pres gpt. i tak nevim v cem to bylo
#ale pravdepodobne chyby z nepozornosti. To je muj nejvetsi problem.
#ukol stejny jak ukol 1
class Lod:
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement

    def strili(self):
        print(f"{self.name} střílí.")

    def zakotvit(self):
        print(f"{self.name} je zakotvena.")

    def __str__(self):
        return f"Loď: {self.name}, délka: {self.length}m, výtlak: {self.displacement}t"
class Fregata(Lod):
    def __init__(self, name, length, displacement, zbrane):
        super().__init__(name, length, displacement)
        self.zbrane = zbrane

    def odpalit_raketu(self):
        print(f"{self.name} odpaluje raketu pomocí systému {self.zbrane}.")

    def __str__(self):
        return f"{super().__str__()}, zbraňový systém: {self.zbrane}"
class Destroyer(Lod):
    def __init__(self, name, length, displacement, torpedo_tubes):
        super().__init__(name, length, displacement)
        self.torpedo_tubes = torpedo_tubes

    def odpalit_torpedo(self):
        print(f"{self.name} odpaluje torpédo z jednoho z {self.torpedo_tubes} torpédometů.")

    def __str__(self):
        return f"{super().__str__()}, počet torpédometů: {self.torpedo_tubes}"
class Cruiser(Lod):
    def __init__(self, name, length, displacement, artillery_caliber):
        super().__init__(name, length, displacement)
        self.artillery_caliber = artillery_caliber

    def strilet_z_del(self):
        print(f"{self.name} střílí z děl ráže {self.artillery_caliber}mm.")

    def __str__(self):
        return f"{super().__str__()}, ráže děl: {self.artillery_caliber}mm"

fregata = Fregata("Fregata Clinton", 100, 1000, "XXX")
destroyer = Destroyer("Terminator", 200, 2000, 200)
cruiser = Cruiser("XXX", 1, 11111, 111)

print(fregata)
fregata.strili()
fregata.odpalit_raketu()
fregata.zakotvit()

print(destroyer)
destroyer.strili()
destroyer.odpalit_torpedo()
destroyer.zakotvit()

print(cruiser)
cruiser.strili()
cruiser.strilet_z_del()
cruiser.zakotvit()
