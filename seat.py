class Seat:
    """O'rindiq va uning bandlik holati."""

    VIP_KOEFFITSIENT = 1.5  # VIP o'rindiq standartdan 1.5 barobar qimmat

    def __init__(self, id, qator, raqam, turi, asosiy_narx):
        if turi not in ("Standard", "VIP"):
            raise ValueError("O'rindiq turi Standard yoki VIP bo'lishi kerak!")
        self.__id = id
        self.__qator = qator
        self.__raqam = raqam
        self.__turi = turi
        self.__asosiy_narx = asosiy_narx
        self.__band = False
        self.__narxi = self.narxni_aniqlash()

    @property
    def id(self):
        return self.__id

    @property
    def qator(self):
        return self.__qator

    @property
    def raqam(self):
        return self.__raqam

    @property
    def turi(self):
        return self.__turi

    @property
    def narxi(self):
        return self.__narxi

    @property
    def band(self):
        return self.__band

    def narxni_aniqlash(self):
        if self.__turi == "VIP":
            return self.__asosiy_narx * self.VIP_KOEFFITSIENT
        return self.__asosiy_narx

    def malumot(self):
        holat = "Band" if self.__band else "Bo'sh"
        return (
            f"[{self.__id}] {self.__qator}-qator, {self.__raqam}-o'rin | "
            f"{self.__turi} | {self.__narxi:,.0f} so'm | {holat}"
        )

    def band_qilish(self):
        if self.__band:
            raise ValueError("Bu o'rindiq allaqachon band!")
        self.__band = True

    def boshatish(self):
        self.__band = False
