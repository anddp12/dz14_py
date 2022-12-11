# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в пёолях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 

class Car:
    def __init__(self, model, year_manufacture, make, capacity, color, price):
        self.model = model
        self.year = year_manufacture
        self.make = make
        self.capacity = capacity
        self.color = color
        self.price = price
    
    def auto(self):
        print(f'Модель {self.model}, {self.year} года выпуска, производителя {self.make}, объемом двигателя {self.capacity} литра, цвета {self.color}, стоимостью ${self.price}')

car1 = Car("Accord", "2008", "Honda", "2.0", "black", "9200")

car1.auto()

print(f'Марка авто {car1.make}, модели {car1.model}, куплена за {car1.price}')

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Book:
    def __init__(self, title, year_manufacture, publisher, genre, autor, price):
        self.title = title
        self.year1 = year_manufacture
        self.pablisher = publisher
        self.genre = genre        
        self.autor = autor
        self.price1 = price

    def book(self):
        print(f'Книга под названием {self.title}, {self.year1} года выпуска, издания {self.pablisher}, жанр {self.genre}, автора {self.autor}, цена {self.price1} грн')

book1 = Book("'Ускоренный курс Python'", "2018", "Старого Лева", "Компьютерная литература", "Маттес Ерік", "360")

book1.book()

print(f'Книга {book1.title}, была выпущена в {book1.year1} году, издательством {book1.pablisher}')

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def stadium(self):
        print(f'Стадион {self.name}, дата открытия {self.opening_date} года, страна {self.country}, город {self.city}, вместимостью {self.capacity} человек')

stadium1 = Stadium("'Сан-Сиро'", "1899", "Италия", "Милан", "80018")

stadium1.stadium()

print(f'Стадион {stadium1.name}, принимал финал Лиги Чемпионов УЕФА в 2001 году')