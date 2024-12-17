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

#Пример использования:
if __name__ == "__main__":
    encyclopedia = Encyclopedia("Энциклопедия", 200, 2, 100, 10000)
    phone_directory = PhoneDirectory("Телефонный справочник",80, 2, 0, 8000)
    print(f"Время чтения энциклопедии '{encyclopedia.title}': {encyclopedia.reading_time()} минут")
    print(f"Статей на странице: {encyclopedia.articles_per_page()}")

    print(f"Время чтения телефонного справочника '{phone_directory.title}': {phone_directory.reading_time()} минут")
    print(f"Номеров на странице: {phone_directory.articles_per_page()}")