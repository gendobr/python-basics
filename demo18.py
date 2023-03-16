"""
Авіарейс (Звідки, куди, дата, час, номер, кількість_пасажирів)
"""


class Flight:
    departure_place: str  # Звідки
    arrival_place: str  # куди
    departure_datetime: str  # дата, час відправлення
    arrival_datetime: str  # дата, час прибуття
    uid: str  # номер
    n_passengers: int  # кількість_пасажирів

    # конструктор
    def __init__(
        self,
        *,
        departure_place: str,  # Звідки
        arrival_place: str,  # куди
        departure_datetime: str,  # дата, час відправлення
        arrival_datetime: str,  # дата, час прибуття
        uid: str,  # номер
        n_passengers: int,  # кількість_пасажирів
    ) -> None:
        self.arrival_datetime = departure_place
        self.arrival_datetime = arrival_place
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.uid = uid
        self.n_passengers = n_passengers
        self.__checkin()
        self._checkout()

    # private
    def __checkin(self):
        self.n_passengers = self.n_passengers + 1

    # protected
    def _checkout(self):
        self.n_passengers = self.n_passengers - 1

    def set_departure_datetime(self, new_value):
        self.departure_datetime = new_value

    def set_arrival_datetime(self, new_value):
        self.arrival_datetime = new_value


class FlightExt(Flight):
    real_departure_datetime: str  # дата, час відправлення
    real_arrival_datetime: str  # дата, час прибуття

    def __init__(
        self,
        *,
        departure_place: str,  # Звідки
        arrival_place: str,  # куди
        departure_datetime: str,  # дата, час відправлення
        arrival_datetime: str,  # дата, час прибуття
        uid: str,  # номер
        n_passengers: int,  # кількість_пасажирів
        real_departure_datetime,
        real_arrival_datetime,
    ) -> None:
        super(FlightExt, self).__init__(
            departure_place=departure_place,  # Звідки
            arrival_place=arrival_place,  # куди
            departure_datetime=departure_datetime,
            arrival_datetime=arrival_datetime,
            uid=uid,  # номер
            n_passengers=n_passengers,  # кількість_пасажирів
        )
        self.real_departure_datetime = real_departure_datetime
        self.real_arrival_datetime = real_arrival_datetime

    # departure_place: str  # Звідки
    # arrival_place: str  # куди
    # departure_datetime: str  # дата, час відправлення
    # arrival_datetime: str  # дата, час прибуття
    # uid: str  # номер
    # n_passengers: int  # кількість_пасажирів
    # # конструктор
    # def __init__(
    #     self,
    #     *,
    #     departure_place: str,  # Звідки
    #     arrival_place: str,  # куди
    #     departure_datetime: str,  # дата, час відправлення
    #     arrival_datetime: str,  # дата, час прибуття
    #     uid: str,  # номер
    #     n_passengers: int,  # кількість_пасажирів
    # ) -> None:
    #     self.arrival_datetime = departure_place
    #     self.arrival_datetime = arrival_place
    #     self.departure_datetime = departure_datetime
    #     self.arrival_datetime = arrival_datetime
    #     self.uid = uid
    #     self.n_passengers = n_passengers
    #     self.__checkin()
    #     self._checkout()
    # # private
    # def __checkin(self):
    #     self.n_passengers = self.n_passengers + 1

    # # protected
    # def _checkout(self):
    #     self.n_passengers = self.n_passengers - 1

    # def set_departure_datetime(self, new_value):
    #     self.departure_datetime = new_value

    # def set_arrival_datetime(self, new_value):
    #     self.arrival_datetime = new_value


FlightD127 = FlightExt(
    departure_place="ZP",  # Звідки
    arrival_place="LV",  # куди
    departure_datetime="2023-05-02 12:45:00",
    arrival_datetime="2023-05-02 13:45:00",
    uid="D127",  # номер
    n_passengers=0,  # кількість_пасажирів
)

print(FlightD127.n_passengers)
for i in range(0, 32):
    FlightD127.__checkin()
    print(FlightD127.n_passengers)


print(FlightD127.n_passengers)
for i in range(0, 32):
    FlightD127._checkout()
    print(FlightD127.n_passengers)


print(FlightD127.departure_datetime)
FlightD127.set_departure_datetime("2023-05-02 13:45:00")
print(FlightD127.departure_datetime)
