from data import malumotlarni_yuklash


def son_kirit(matn):
    """Faqat butun son qabul qiladi (input validation)."""
    while True:
        try:
            return int(input(matn))
        except ValueError:
            print("Xato: faqat butun son kiriting!")


class CinemaApp:
    def __init__(self):
        self.__filmlar, self.__zallar, self.__mijoz = malumotlarni_yuklash()
        self.__tanlangan_film = None

    # ---------- yordamchi metodlar ----------
    def __film_topish(self, film_id):
        for film in self.__filmlar:
            if film.id == film_id:
                return film
        raise ValueError("Bunday ID li film mavjud emas!")

    def __film_tanlanganini_tekshirish(self):
        if self.__tanlangan_film is None:
            raise ValueError("Avval 2-bo'limdan film tanlang!")
        return self.__tanlangan_film

    def __orindiqlar_royxati(self):
        film = self.__film_tanlanganini_tekshirish()
        return self.__zallar[film.id]

    def __orindiq_topish(self, orindiq_id):
        for seat in self.__orindiqlar_royxati():
            if seat.id == orindiq_id:
                return seat
        raise ValueError("Bunday ID li o'rindiq mavjud emas!")

    # ---------- menu amallari ----------
    def filmlarni_korish(self):
        print("\n--- Barcha filmlar ---")
        for film in self.__filmlar:
            print(film.malumot())

    def film_tanlash(self):
        self.filmlarni_korish()
        film_id = son_kirit("\nFilm ID sini kiriting: ")
        self.__tanlangan_film = self.__film_topish(film_id)
        print(f"Tanlandi: {self.__tanlangan_film.nomi}")

    def orindiqlarni_korish(self, faqat_bosh=False):
        orindiqlar = self.__orindiqlar_royxati()
        nom = self.__tanlangan_film.nomi
        print(f"\n--- {nom}: {'bo`sh' if faqat_bosh else 'barcha'} o'rindiqlar ---")
        korsatildi = False
        for seat in orindiqlar:
            if faqat_bosh and seat.band:
                continue
            print(seat.malumot())
            korsatildi = True
        if not korsatildi:
            print("Bo'sh o'rindiq qolmagan.")

    def bosh_orindiqlarni_korish(self):
        self.orindiqlarni_korish(faqat_bosh=True)

    def orindiq_bron_qilish(self):
        film = self.__film_tanlanganini_tekshirish()
        self.bosh_orindiqlarni_korish()
        seat_id = son_kirit("\nO'rindiq ID sini kiriting: ")
        seat = self.__orindiq_topish(seat_id)
        bron = self.__mijoz.bron_qilish(film, seat)
        print("Bron muvaffaqiyatli amalga oshdi!")
        print(bron.malumot())

    def mening_bronlarim(self):
        print("\n--- Mening bronlarim ---")
        self.__mijoz.bronlarni_korish()

    def bronni_bekor_qilish(self):
        self.mening_bronlarim()
        bron_id = son_kirit("\nBekor qilinadigan bron ID sini kiriting: ")
        bron = self.__mijoz.bronni_bekor_qilish(bron_id)
        print(f"Bron #{bron.id} bekor qilindi, pul qaytarildi.")

    def balansni_korish(self):
        print(self.__mijoz.balansni_korish())

    # ---------- asosiy sikl ----------
    def ishga_tushirish(self):
        amallar = {
            1: self.filmlarni_korish,
            2: self.film_tanlash,
            3: self.orindiqlarni_korish,
            4: self.bosh_orindiqlarni_korish,
            5: self.orindiq_bron_qilish,
            6: self.mening_bronlarim,
            7: self.bronni_bekor_qilish,
            8: self.balansni_korish,
        }
        while True:
            print(f"\n=== Cinema Booking System === (Mijoz: {self.__mijoz.nomi})")
            if self.__tanlangan_film:
                print(f"Tanlangan film: {self.__tanlangan_film.nomi}")
            print("1. Barcha filmlarni ko'rish")
            print("2. Film tanlash")
            print("3. Barcha o'rindiqlarni ko'rish")
            print("4. Bo'sh o'rindiqlarni ko'rish")
            print("5. O'rindiq bron qilish")
            print("6. Mening bronlarim")
            print("7. Bronni bekor qilish")
            print("8. Balansni ko'rish")
            print("9. Dasturni yakunlash")

            tanlov = son_kirit("Tanlang: ")
            if tanlov == 9:
                print("Xayr! Yana kutamiz.")
                break
            amal = amallar.get(tanlov)
            if amal is None:
                print("Xato: 1 dan 9 gacha son kiriting!")
                continue
            try:
                amal()
            except ValueError as xato:
                print(f"Xatolik: {xato}")


if __name__ == "__main__":
    CinemaApp().ishga_tushirish()
