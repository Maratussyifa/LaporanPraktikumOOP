class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat Private
        self.__hp = hp_awal

    # GETTER
    def get_hp(self):
        return self.__hp

    # SETTER (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# ===== UJI COBA =====
hero1 = Hero("Layla", 100)

# 1️⃣ Percobaan Hacking (Name Mangling)
print(f"Mencoba akses paksa: {hero1._Hero__hp}")  # Akan MUNCUL

# 2️⃣ Uji Validasi Setter
hero1.set_hp(-100)
print(f"HP setelah set -100: {hero1.get_hp()}")


# ===== Versi Setter TANPA Validasi (untuk eksperimen 2) =====
class HeroTanpaValidasi:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    # SETTER TANPA IF/ELIF
    def set_hp(self, nilai_baru):
        self.__hp = nilai_baru


hero2 = HeroTanpaValidasi("Miya", 100)
hero2.set_hp(-100)
print(f"HP Miya tanpa validasi: {hero2.get_hp()}")  # Akan jadi -100
