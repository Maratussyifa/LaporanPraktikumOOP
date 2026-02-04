from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # WAJIB ada (kalau dihapus → error)
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
# unit = GameUnit()  # AKTIFKAN untuk eksperimen nomor 2

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()
