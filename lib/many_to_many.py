class Author:
    all_authors = []
    
    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)
        
    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []
    
    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)
        
    def contracts(self):
        return self._contracts
    
    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all_contracts = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book):
            raise Exception("Author and Book must be of type Author and Book")
        if not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Date and Royalties must be of type str and int")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
        
        author._contracts.append(self)
        book._contracts.append(self)
        
    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Date must be of type str")
        contracts = [contract for contract in cls.all_contracts if contract.date == date]
        return sorted(contracts, key=lambda x: x.date)