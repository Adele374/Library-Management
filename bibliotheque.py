"""
Library Management System
Group Assignment 1 - Advanced Programming
"""

# Part 2: Inheritance - Parent Class
class Document:
    """Parent class representing a generic document in the library."""

    def __init__(self, title, author, year, code):
        self.title = title
        self.author = author
        self.year = year
        self.code = code
        self.borrowed = False

    # Part 3: Magic Method __str__
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {status}"

    # Part 3: Magic Method __eq__
    def __eq__(self, other):
        """Compare two documents by their unique code."""
        if isinstance(other, Document):
            return self.code == other.code
        return False

    def borrow(self):
        """Mark the document as borrowed."""
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_item(self):
        """Mark the document as returned."""
        if self.borrowed:
            self.borrowed = False
            return True
        return False

    # Part 4: @staticmethod decorator
    @staticmethod
    def validate_year(year):
        """Validate that a year is reasonable for a document."""
        current_year = 2026
        return 1000 <= year <= current_year


"""
Library Management System
Group Assignment 1 - Advanced Programming
COMMIT 2: Added Book child class with inheritance and magic methods
"""

# Part 2: Inheritance - Parent Class
class Document:
    """Parent class representing a generic document in the library."""

    def __init__(self, title, author, year, code):
        self.title = title
        self.author = author
        self.year = year
        self.code = code
        self.borrowed = False

    # Part 3: Magic Method __str__
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {status}"

    # Part 3: Magic Method __eq__
    def __eq__(self, other):
        """Compare two documents by their unique code."""
        if isinstance(other, Document):
            return self.code == other.code
        return False

    def borrow(self):
        """Mark the document as borrowed."""
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_item(self):
        """Mark the document as returned."""
        if self.borrowed:
            self.borrowed = False
            return True
        return False

    # Part 4: @staticmethod decorator
    @staticmethod
    def validate_year(year):
        """Validate that a year is reasonable for a document."""
        current_year = 2026
        return 1000 <= year <= current_year


# Part 2: Inheritance - Child Class
class Book(Document):
    """Child class representing a book (inherits from Document)."""

    def __init__(self, title, author, year, code, num_pages, isbn):
        # Call the parent constructor with super()
        super().__init__(title, author, year, code)
        # New attributes specific to books
        self.num_pages = num_pages
        self.isbn = isbn

    # Part 3: Magic Method __str__ (override)
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {self.num_pages} pages - ISBN: {self.isbn} - {status}"

    # Part 3: Magic Method __len__
    def __len__(self):
        """Return the number of pages in the book."""
        return self.num_pages

    # New method specific to books
    def is_long(self):
        """Determine if the book is considered long."""
        return self.num_pages > 300

    # Part 4: @property decorator
    @property
    def full_description(self):
        """Return a complete description of the book."""
        length = "long" if self.is_long() else "short"
        return f"{self.title} is a {length} book of {self.num_pages} pages written by {self.author}."
    
    """
Library Management System
Group Assignment 1 - Advanced Programming
COMMIT 3: Added Member class with decorators
"""

# Part 2: Inheritance - Parent Class
class Document:
    """Parent class representing a generic document in the library."""

    def __init__(self, title, author, year, code):
        self.title = title
        self.author = author
        self.year = year
        self.code = code
        self.borrowed = False

    # Part 3: Magic Method __str__
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {status}"

    # Part 3: Magic Method __eq__
    def __eq__(self, other):
        """Compare two documents by their unique code."""
        if isinstance(other, Document):
            return self.code == other.code
        return False

    def borrow(self):
        """Mark the document as borrowed."""
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_item(self):
        """Mark the document as returned."""
        if self.borrowed:
            self.borrowed = False
            return True
        return False

    # Part 4: @staticmethod decorator
    @staticmethod
    def validate_year(year):
        """Validate that a year is reasonable for a document."""
        current_year = 2026
        return 1000 <= year <= current_year


# Part 2: Inheritance - Child Class
class Book(Document):
    """Child class representing a book (inherits from Document)."""

    def __init__(self, title, author, year, code, num_pages, isbn):
        # Call the parent constructor with super()
        super().__init__(title, author, year, code)
        # New attributes specific to books
        self.num_pages = num_pages
        self.isbn = isbn

    # Part 3: Magic Method __str__ (override)
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f" {self.title} by {self.author} ({self.year}) - {self.num_pages} pages - ISBN: {self.isbn} - {status}"

    # Part 3: Magic Method __len__
    def __len__(self):
        """Return the number of pages in the book."""
        return self.num_pages

    # New method specific to books
    def is_long(self):
        """Determine if the book is considered long."""
        return self.num_pages > 300

    # Part 4: @property decorator
    @property
    def full_description(self):
        """Return a complete description of the book."""
        length = "long" if self.is_long() else "short"
        return f"{self.title} is a {length} book of {self.num_pages} pages written by {self.author}."


# Part 4: @classmethod decorator
class Member:
    """Class representing a library member."""

    # Class variable to count members
    total_members = 0

    def __init__(self, last_name, first_name, age, member_number):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.member_number = member_number
        self.borrowed_books = []
        Member.total_members += 1

    # Part 3: Magic Method __str__
    def __str__(self):
        return f" {self.first_name} {self.last_name} (#{self.member_number}) - {len(self.borrowed_books)} book(s) borrowed"

    # Part 4: @classmethod decorator
    @classmethod
    def get_total_members(cls):
        """Return the total number of registered members."""
        return cls.total_members

    def can_borrow(self, max_books=3):
        """Check if the member can borrow more books."""
        return len(self.borrowed_books) < max_books