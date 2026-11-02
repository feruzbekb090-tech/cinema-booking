from movie import Movie
from seat import Seat
from customer import Customer


def filmlarni_yaratish():
    return [
        Movie(
            1,
            "Interstellar",
            "Fantastika",
            169,
            8.7,
            "Koinotda yangi uy izlayotgan sayohatchilar haqida.",
            40000,
        ),
        Movie(
            2,
            "Inception",
            "Triller",
            148,
            8.8,
            "Tush ichidagi tushlar olamida o'g'rilik.",
            35000,
        ),
        Movie(
            3,
            "The Lion King",
            "Multfilm",
            88,
            8.5,
            "Sher bolasi Simbaning taxtga yo'li.",
            30000,
        ),
        Movie(
            4,
            "John Wick",
            "Jangari",
            101,
            7.4,
            "Sobiq qotilning qasos hikoyasi.",
            35000,
        ),
    ]


def zalni_yaratish(asosiy_narx, boshlangich_id, qatorlar=5, ustunlar=6, vip_qatorlar=2):
    """Bitta film seansi uchun o'rindiqlar ro'yxatini yaratadi."""
    orindiqlar = []
    id_ = boshlangich_id
    for qator in range(1, qatorlar + 1):
        turi = "VIP" if qator > qatorlar - vip_qatorlar else "Standard"
        for raqam in range(1, ustunlar + 1):
            orindiqlar.append(Seat(id_, qator, raqam, turi, asosiy_narx))
            id_ += 1
    return orindiqlar


def malumotlarni_yuklash():
    """(filmlar, zallar, mijoz) ni qaytaradi. O'rindiq ID lari barcha seanslarda unikal."""
    filmlar = filmlarni_yaratish()
    zallar = {}
    keyingi_id = 1
    for film in filmlar:
        zal = zalni_yaratish(film.narxi, keyingi_id)
        zallar[film.id] = zal
        keyingi_id += len(zal)
    mijoz = Customer(1, "Ali Valiyev", "+998901234567", 500000)
    return filmlar, zallar, mijoz
