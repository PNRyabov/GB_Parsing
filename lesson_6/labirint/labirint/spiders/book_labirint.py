import scrapy


class BookLabirintSpider(scrapy.Spider):
    name = 'book_labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/books']

    def parse(self, response):
        pass

#
# 1) Создать пауков по сбору данных о книгах с сайтов labirint.ru и/или book24.ru
# 2) Каждый паук должен собирать:
# * Ссылку на книгу
# * Наименование книги
# * Автор(ы)
# * Основную цену
# * Цену со скидкой
# * Рейтинг книги
# 3) Собранная информация должна складываться в базу данных