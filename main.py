# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. 
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
        print(f'Модель {self.model}, {self.year} года выпуска, производителя {self.make}, объемом двигателя {self.capacity} литра, цвета {self.color}, стоимостью {self.price}')



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
        print(f'Книга под названием {self.title}, {self.year1} года выпуска, издателя {self.pablisher}, жанр {self.genre}, автора {self.autor}, цена {self.price1} грн')


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
        print(f'Стадион {self.name}, дата открытия {self.opening_date}, страна {self.country}, город {self.city}, вместимостью {self.capacity} человек')



