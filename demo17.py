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

    # метод
    def checkin(self):
        self.n_passengers = self.n_passengers + 1

    # метод
    def checkout(self):
        self.n_passengers = self.n_passengers - 1

    # метод
    def set_departure_datetime(self, new_value):
        self.departure_datetime = new_value

    def set_arrival_datetime(self, new_value):
        self.arrival_datetime = new_value


FlightD127 = Flight(
    departure_place="ZP",  # Звідки
    arrival_place="LV",  # куди
    departure_datetime="2023-05-02 12:45:00",
    arrival_datetime="2023-05-02 13:45:00",
    uid="D127",  # номер
    n_passengers=0,  # кількість_пасажирів
)

print(FlightD127.n_passengers)
for i in range(0, 32):
    FlightD127.checkin()
    print(FlightD127.n_passengers)

print(FlightD127.departure_datetime)
FlightD127.set_departure_datetime("2023-05-02 13:45:00")
print(FlightD127.departure_datetime)
