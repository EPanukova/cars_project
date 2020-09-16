class Carbase:
    """Базовый класс"""
    def __init__(self, car_type=None, brand=None, photo_le_name=None):
        """Метод иниц"""
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name


    def get_photo_le_ext(self):
        """Возвращает расширение"""
        result = self.photo_le_name.find('.')
        if result == -1:
            return None
        else:
            return self.photo_le_name[result:]


class Car(Carbase):
    """Класс легковых"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None):
        """Метод иниц"""
        super().__init__(car_type, brand, photo_le_name)
        self.passenger_seats_count = int(passenger_seats_count) or None
        self.carrying = float(carrying) or None


class Truck(Carbase):
    """Класс грузовых"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl, carrying):
        """Метод иниц"""
        super().__init__(car_type, photo_le_name, brand)
        self.body_whl = body_whl or None
        if self.body_whl is not None:
            try:
                self.body_whl = body_whl.split('x')
                self.body_width, self.body_height, self.body_lenght = float(self.body_whl[0]), float(self.body_whl[1]), float(self.body_whl[2])
            except:
                self.body_width, self.body_height, self.body_lenght = 0.0, 0.0, 0.0
        else:
            self.body_width, self.body_height, self.body_lenght = 0.0, 0.0, 0.0
        self.carrying = float(carrying)

    def get_body_volume(self):
        """Возвращает объем кузова"""
        return float(self.body_width * self.body_height * self.body_lenght)


class Specmachine(Carbase):
    """Класс спецтехники"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None, extra=None):
        super().__init__(car_type, photo_le_name, brand)
        self.extra = extra or None
        self.carrying = float(carrying) or None


def get_car_list(filename):
    """Метод считывает данные из файла"""
    car_list = []
    with open(filename, encoding='utf-8') as inp_file:
        for line in inp_file:
            lst = line.split(';')
            try:
                if lst[0] == 'car':
                    car_list.append(Car(*lst[:-1]))
            except TypeError:
                pass

            try:
                if lst[0] == 'truck':
                    car_list.append(Truck(*lst[:-1]))
            except TypeError:
                pass

            try:
                if lst[0] == 'spec_machine':
                    car_list.append(Specmachine(*lst[:-1]))
            except TypeError:
                pass

    return car_list


def main():
    get_car_list('solution.txt')

if __name__ == '__main__':
    main()
