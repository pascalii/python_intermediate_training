from abc import ABC, abstractmethod


class Osoba(ABC):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"

    @abstractmethod
    def pokaz_finanse(self):
        pass


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie: str, wiek: int, stypendium: int):
        super().__init__(imie, wiek)
        self.stypendium = stypendium
        imie: str = self.imie

    def pokaz_finanse(self):
        return self.stypendium, self.imie


def main():
    pracownik = Pracownik('mike', 29, 20, 168)
    pracownik2 = Pracownik('mike2', 29, 50, 168)
    student = Student('sarah', 29, 505)
    student2 = Student('sarah2', 29, 520)
    person_list = [pracownik, pracownik2, student, student2]
    for person in person_list:
        print(person.pokaz_finanse())


print(main())
