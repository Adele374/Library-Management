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