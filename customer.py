from booking import Booking


class Customer:
    """Mijoz, uning balansi va bronlari."""

    def __init__(self, id, nomi, telefoni, puli):
        self.__id = id
        self.__nomi = nomi
        self.__telefoni = telefoni
        self.__puli = puli
        self.__bronlar = []

    @property
    def id(self):
        return self.__id

    @property
    def nomi(self):
        return self.__nomi

    @property
    def telefoni(self):
        return self.__telefoni

    @property
    def puli(self):
        return self.__puli

    @property
    def bronlar(self):
        return list(self.__bronlar)  # nusxa qaytaradi (encapsulation)

    def pul_yechish(self, summa):
        if summa > self.__puli:
            raise ValueError("Mablag' yetarli emas!")
        self.__puli -= summa

    def pul_qaytarish(self, summa):
        self.__puli += summa

    def bron_qilish(self, movie, seat):
        bron = Booking(self, movie, seat)
        bron.bron_qilish()  # xatolik bo'lsa shu yerda ko'tariladi
        self.__bronlar.append(bron)
        return bron

    def bronlarni_korish(self):
        if not self.__bronlar:
            print("Sizda hali bronlar yo'q.")
            return
        for bron in self.__bronlar:
            print(bron.malumot())

    def bronni_bekor_qilish(self, bron_id):
        for bron in self.__bronlar:
            if bron.id == bron_id:
                bron.bekor_qilish()
                return bron
        raise ValueError("Bunday ID li bron topilmadi!")

    def balansni_korish(self):
        return f"Balansingiz: {self.__puli:,.0f} so'm"
