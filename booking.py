class Booking:
    """Bitta bron jarayoni: mijoz + film + o'rindiq."""

    __keyingi_id = 1

    def __init__(self, customer, movie, seat):
        self.__id = Booking.__keyingi_id
        Booking.__keyingi_id += 1
        self.__customer = customer
        self.__movie = movie
        self.__seat = seat
        self.__narxi = seat.narxi
        self.__status = "Pending"

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer

    @property
    def movie(self):
        return self.__movie

    @property
    def seat(self):
        return self.__seat

    @property
    def narxi(self):
        return self.__narxi

    @property
    def status(self):
        return self.__status

    def malumot(self):
        return (
            f"Bron #{self.__id} | {self.__movie.nomi} | "
            f"{self.__seat.qator}-qator {self.__seat.raqam}-o'rin ({self.__seat.turi}) | "
            f"{self.__narxi:,.0f} so'm | {self.__status}"
        )

    def bron_qilish(self):
        """Barcha shartlarni tekshiradi va bronni amalga oshiradi."""
        # Mijoz shu o'rindiqni allaqachon bron qilganmi?
        for b in self.__customer.bronlar:
            if b.status == "Active" and b.seat.id == self.__seat.id:
                raise ValueError("Siz bu o'rindiqni allaqachon bron qilgansiz!")
        if self.__seat.band:
            raise ValueError("Bu o'rindiq band, boshqasini tanlang!")
        if self.__customer.puli < self.__narxi:
            raise ValueError("Balansingizda mablag' yetarli emas!")

        self.__seat.band_qilish()
        self.__customer.pul_yechish(self.__narxi)
        self.__status = "Active"

    def bekor_qilish(self):
        if self.__status != "Active":
            raise ValueError("Bu bron allaqachon bekor qilingan!")
        self.__seat.boshatish()
        self.__customer.pul_qaytarish(self.__narxi)
        self.__status = "Cancelled"
