class Movie:
    """Kinoteatrda namoyish qilinadigan film."""

    def __init__(self, id, nomi, janri, davomiyligi, reyting, tavsif, narxi):
        self.__id = id
        self.__nomi = nomi
        self.__janri = janri
        self.__davomiyligi = davomiyligi
        self.__reyting = reyting
        self.__tavsif = tavsif
        self.__narxi = narxi

    @property
    def id(self):
        return self.__id

    @property
    def nomi(self):
        return self.__nomi

    @property
    def janri(self):
        return self.__janri

    @property
    def davomiyligi(self):
        return self.__davomiyligi

    @property
    def reyting(self):
        return self.__reyting

    @property
    def tavsif(self):
        return self.__tavsif

    @property
    def narxi(self):
        return self.__narxi

    def malumot(self):
        return (
            f"[{self.__id}] {self.__nomi} | Janr: {self.__janri} | "
            f"{self.__davomiyligi} min | Reyting: {self.__reyting} | "
            f"Narx: {self.__narxi:,.0f} so'm\n    {self.__tavsif}"
        )

    def reytingni_ozgartirish(self, yangi_reyting):
        if not 0 <= yangi_reyting <= 10:
            raise ValueError("Reyting 0 dan 10 gacha bo'lishi kerak!")
        self.__reyting = yangi_reyting
