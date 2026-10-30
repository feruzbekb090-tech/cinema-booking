# Cinema Booking System

## 1. Project haqida

**Cinema Booking System** — mijozlarga kinoteatrdagi filmlarni ko‘rish, o‘rindiqlarni tanlash va bron qilish imkonini beruvchi Console-based Python application.

Dastur orqali mijoz mavjud filmlarni ko‘rishi, film tanlashi, bo‘sh o‘rindiqlarni tekshirishi, chipta bron qilishi va bronni bekor qilishi mumkin.

### Project maqsadi

- Class va Object bilan ishlash.
- Attributes va Methods yaratish.
- Obyektlar o‘rtasida munosabat tashkil qilish.
- Encapsulation tamoyilini qo‘llash.
- Modular programming.
- Real-world business logic yaratish.

---

## 2. Project imkoniyatlari

### Customer imkoniyatlari

1. Barcha filmlarni ko‘rish.
2. Film haqida ma'lumot olish.
3. Film tanlash.
4. Barcha o‘rindiqlarni ko‘rish.
5. Bo‘sh o‘rindiqlarni ko‘rish.
6. O‘rindiq tanlash.
7. Chipta bron qilish.
8. O‘z bronlarini ko‘rish.
9. Bronni bekor qilish.
10. Balansni ko‘rish.

---

## 3. File Structure

    cinema_booking/
    │
    ├── main.py
    ├── movie.py
    ├── seat.py
    ├── customer.py
    ├── booking.py
    └── data.py

### Fayllarning vazifalari

| File | Vazifasi |
|---|---|
| main.py | Dasturni ishga tushirish va menu |
| movie.py | Film classi |
| seat.py | O‘rindiqlarni boshqarish |
| customer.py | Mijozlar bilan ishlash |
| booking.py | Bron qilish jarayoni |
| data.py | Boshlang‘ich ma'lumotlar va obyektlar |

---

## 4. Classes, Attributes & Methods

### 4.1. Movie Class

**Vazifasi:** Kinoteatrda namoyish qilinadigan filmlar haqidagi ma'lumotlarni saqlash.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | Film ID |
| nomi | str | Film nomi |
| janri | str | Film janri |
| davomiyligi | int | Film davomiyligi (minut) |
| reyting | float | Film reytingi |
| tavsif | str | Film haqida ma'lumot |
| narxi | float | Chipta uchun asosiy narx |

**Methods:**

- `malumot()` — film haqida ma'lumot chiqarish.
- `reytingni_ozgartirish()` — film reytingini yangilash.

### 4.2. Seat Class

**Vazifasi:** O‘rindiqlarning xususiyatlari va bandlik holatini boshqarish.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | O‘rindiq ID |
| qator | int | O‘rindiq joylashgan qator |
| raqam | int | Qatordagi o‘rindiq raqami |
| turi | str | Standard yoki VIP |
| narxi | float | O‘rindiq narxi |
| band | bool | O‘rindiq band yoki bo‘shligi |

**Methods:**

- `malumot()` — o‘rindiq haqida ma'lumot chiqarish.
- `band_qilish()` — o‘rindiqni band qilish.
- `boshatish()` — o‘rindiqni bo‘shatish.
- `narxni_aniqlash()` — o‘rindiq narxini aniqlash.

### 4.3. Customer Class

**Vazifasi:** Mijozlar va ularning bronlarini boshqarish.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | Mijoz ID |
| nomi | str | Mijoz ismi |
| telefoni | str | Telefon raqami |
| puli | float | Mijoz balansi |
| bronlar | list | Mijozning bronlari |

**Methods:**

- `bron_qilish()` — o‘rindiq bron qilish.
- `bronlarni_korish()` — barcha bronlarni ko‘rish.
- `bronni_bekor_qilish()` — bronni bekor qilish.
- `balansni_korish()` — mijoz balansini ko‘rish.

### 4.4. Booking Class

**Vazifasi:** Mijozning film va o‘rindiq tanlovi asosida bron jarayonini boshqarish.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | Bron ID |
| customer | Customer | Bron qilgan mijoz |
| movie | Movie | Tanlangan film |
| seat | Seat | Tanlangan o‘rindiq |
| narxi | float | Bron narxi |
| status | str | Active yoki Cancelled |

**Methods:**

- `malumot()` — bron haqida ma'lumot chiqarish.
- `bron_qilish()` — bronni amalga oshirish.
- `bekor_qilish()` — bronni bekor qilish.

---

## 5. Main Menu

Dastur ishga tushganda quyidagi menu chiqishi kerak:

### Cinema Booking System

1. Barcha filmlarni ko‘rish
2. Film tanlash
3. Barcha o‘rindiqlarni ko‘rish
4. Bo‘sh o‘rindiqlarni ko‘rish
5. O‘rindiq bron qilish
6. Mening bronlarim
7. Bronni bekor qilish
8. Balansni ko‘rish
0. Dasturni yakunlash

---

## 6. Business Rules

1. Har bir filmning unikal ID raqami bo‘lishi kerak.
2. Har bir o‘rindiqning unikal ID raqami bo‘lishi kerak.
3. Band qilingan o‘rindiqni qayta bron qilib bo‘lmasligi kerak.
4. Mijozning puli yetarli bo‘lmasa, bron amalga oshmasligi kerak.
5. Bron muvaffaqiyatli amalga oshganda mijoz balansidan pul ayrilishi kerak.
6. Bron bekor qilinganda mijozga pul qaytarilishi kerak.
7. Bekor qilingan bron o‘rindig‘i qayta bo‘shatilishi kerak.
8. VIP o‘rindiqlar oddiy o‘rindiqlardan qimmatroq bo‘lishi kerak.
9. Mavjud bo‘lmagan ID tanlanganda xatolik haqida xabar berilishi kerak.
10. Bir mijoz bir xil o‘rindiqni qayta bron qila olmasligi kerak.

---

## 7. Additional Challenges

Asosiy vazifalarni bajargan o‘quvchilar quyidagilarni ham qo‘shishlari mumkin:

- Film janri bo‘yicha qidirish.
- Film nomi bo‘yicha qidirish.
- Eng yuqori reytingli filmni aniqlash.
- Bir vaqtning o‘zida bir nechta o‘rindiq bron qilish.
- Promo code.
- Chegirma tizimi.
- Bronlar tarixini ko‘rish.
- JSON orqali ma'lumotlarni saqlash va yuklash.

---

## 8. Technical Requirements

- Python 3.
- OOP yondashuvi majburiy.
- Har bir class alohida mas'uliyatga ega bo‘lishi kerak.
- Classlar alohida modullarga ajratilishi kerak.
- Kod takrorlanishi minimallashtirilishi kerak.
- Input validation ishlatilishi kerak.
- Exception handling qo‘llanilishi kerak.
- Dastur console menu orqali boshqarilishi kerak.

---

## 9. Evaluation Criteria

| Mezon | Ball |
|---|---:|
| Class va Object | 15 |
| Attributes va Methods | 10 |
| Classlar o‘rtasidagi munosabatlar | 20 |
| OOP tamoyillari | 15 |
| Business Logic | 20 |
| Modular Architecture | 10 |
| Input Validation | 5 |
| Code Readability | 5 |
| **Jami** | **100** |

---

## 10. Expected Result

Loyiha yakunida mijoz filmlarni ko‘rishi, film tanlashi, o‘rindiqlarni tekshirishi, chipta bron qilishi va bronni bekor qilishi mumkin bo‘lgan ishlaydigan Cinema Booking System yaratilishi kerak.

**Asosiy maqsad:** Python OOP yordamida real hayotdagi bron qilish jarayonini modellashtirish.
