#vytvorime class pro pristroj. v podstate vsechno se odkaze na device, resp. dedicnost
class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    def turn_on(self):
        print(f"{self.model} od {self.brand} zapnuto.")

    def turn_off(self):
        print(f"{self.model} od {self.brand} vypnuto.")

    def __str__(self):
        return f"{self.brand} {self.model}, výkon: {self.power}W"
class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity

    def brew_coffee(self):
        print(f"{self.model} právě běží")

    def __str__(self):
        return f"{super().__str__()}, vody: {self.water_capacity}L"

class Blender(Device):
    def __init__(self, brand, model, power, speed_settings):
        super().__init__(brand, model, power)
        self.speed_settings = speed_settings  # počet rychlostních nastavení

    def blend(self):
        print(f"{self.model} mixuje na stupni {self.speed_settings}.")

    def __str__(self):
        return f"{super().__str__()}, rychlosti: {self.speed_settings}"
class MlynekNaMaso(Device):
    def __init__(self, brand, model, power, grinding_capacity):
        super().__init__(brand, model, power)
        self.grinding_capacity = grinding_capacity

    def grind_meat(self):
        print(f"{self.model} mele maso.")

    def __str__(self):
        return f"{super().__str__()}, pomele: {self.grinding_capacity} kg/h"

#TEST - result: /funguje/
coffee_machine = CoffeeMachine("Philips", "5001", 1000, 2)
blender = Blender("LG", "6002", 2000, 20)
mlynek_na_maso = MlynekNaMaso("XXX", "YYYY", 0000, 5)

print(coffee_machine)
coffee_machine.turn_on()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

print(blender)
blender.turn_on()
blender.blend()
blender.turn_off()

print(mlynek_na_maso)
mlynek_na_maso.turn_on()
mlynek_na_maso.grind_meat()
mlynek_na_maso.turn_off()
