class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int, pages: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self._is_available = True
        self._last_read_pages = 0

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available: raise ValueError
        self._is_available = False

    def give_back(self, pages_read: int):
        if pages_read > self.pages: raise ValueError
        self._is_available = True
        self._last_read_pages = pages_read

class Reader:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.pages_read = 0

class Library:
    def __init__(self):
        self.fund = []

    def __len__(self):
        return len(self.fund)

    def add_book(self, book: Book):
        self.fund.append(book)

    def find_by_isbn(self, isbn: str):
        for book in self.fund:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author: str):
        result = []
        for book in self.fund:
            if book.author == author:
                result.append(book)
        return result

    def lend(self, isbn: str, reader: Reader):
        for fund_index in range(len(self.fund)):
            if self.fund[fund_index].isbn == isbn:
                self.fund[fund_index].borrow()
                reader.books.append(self.fund[fund_index])
                return
        raise KeyError

    def take_back(self, isbn: str, reader: Reader, pages_read: int):
        for fund_index in range(len(self.fund)):
            if self.fund[fund_index].isbn == isbn:
                self.fund[fund_index].give_back(pages_read)
                reader.pages_read += pages_read
                reader.books.remove(self.fund[fund_index])
                return
        raise ValueError

    def available(self):
        result = []
        for book in self.fund:
            if book.is_available:
                result.append(book)
        return result

    def unfinished(self):
        result = []
        for book in self.fund:
            if 0 < book.last_read_pages < book.pages and book.is_available:
                print(book.last_read_pages, book.pages)
                result.append(book)
        return result
