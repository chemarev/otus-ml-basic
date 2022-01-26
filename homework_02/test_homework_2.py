import pytest

from homework_02.car import Car
from homework_02.exceptions import CargoOverload, NotEnoughFuel, LowFuelError
from homework_02.plane import Plane


@pytest.fixture
def car():
    return Car(weight=1200, fuel=40, fuel_consumption=8)


@pytest.fixture
def plane():
    return Plane(1200)


class TestCar:
    def test_change_fuel(self, car):
        start_fuel = car.fuel
        distance = 10
        car.move(distance)
        assert car.fuel == start_fuel - (distance/100) * car.fuel_consumption

    def test_low_fuel_error(self, car):
        car.fuel = 0
        with pytest.raises(LowFuelError):
            car.start()

    def test_move(self, car):
        initial_fuel = car.fuel
        distance = 50
        car.move(distance)
        assert car.fuel == (initial_fuel - car.fuel_consumption * distance / 100)

    def test_not_enough_fuel_error(self, car):
        with pytest.raises(NotEnoughFuel):
            car.move((car.fuel/car.fuel_consumption * 100) + 1)

    def test_start(self, car):
        car.start()
        assert car.started


class TestPlane:
    def test_cargo_overload(self, plane):
        with pytest.raises(CargoOverload):
            plane.load_cargo(plane.max_cargo + 1)

    def test_load_cargo(self, plane):
        plane.load_cargo(100)
        assert plane.cargo == 100

    def test_remove_all_cargo(self, plane):
        plane.load_cargo(100)
        plane.remove_all_cargo()
        assert plane.cargo == 0

