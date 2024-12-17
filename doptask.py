class Book:
    def __init__(self, title, num_pages, time_per_page, num_images):
        self.title = title
        self.num_pages = num_pages
        self.time_per_page = time_per_page
        self.num_images = num_images

    def reading_time(self):
        """Метод 1: время чтения книги"""
        total_time = self.num_pages * self.time_per_page
        return total_time
    
    def articles_per_page(self):
        """Метод 2: количество статей/номеров на страницу"""
        return 0
    
#Добавление фрагмента кода по допзаданию
    def __add__(self, other):
        """Перегрузка оператора сложения"""
        if isinstance(other, Book):
            return Book(
                title=f"{self.title} + {other.title}",
                num_pages=self.num_pages + other.num_pages,
                time_per_page=(self.time_per_page + other.time_per_page) / 2,
                num_images=self.num_images + other.num_images
            )
        return NotImplemented


class Encyclopedia(Book):
    def __init__(self, title, num_pages, time_per_page, num_images, num_articles):
        super().__init__(title, num_pages, time_per_page, num_images)
        self.num_articles = num_articles

    def articles_per_page(self):
        if self.num_pages == 0:
            return 0
        return self.num_articles / self.num_pages


class PhoneDirectory(Book):
    def __init__(self, title, num_pages, time_per_page, num_images, num_entries):
        super().__init__(title, num_pages, time_per_page, num_images)
        self.num_entries = num_entries

    def articles_per_page(self):
        if self.num_pages == 0:
            return 0
        return self.num_entries / self.num_pages


#Пример использования
if __name__ == "__main__":
    encyclopedia = Encyclopedia("Энциклопедия", 200, 2, 100, 10000)
    phone_directory = PhoneDirectory("Телефонный справочник",80, 2, 0, 8000)

    combined_book = encyclopedia + phone_directory

    print(f"Сложенная книга: {combined_book.title}")
    print(f"Количество страниц: {combined_book.num_pages}")
    print(f"Время чтения: {combined_book.reading_time()} минут")
    print(f"Количество картинок: {combined_book.num_images}")