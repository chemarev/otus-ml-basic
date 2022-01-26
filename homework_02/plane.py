from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if (new_cargo := self.cargo + cargo) < self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result
