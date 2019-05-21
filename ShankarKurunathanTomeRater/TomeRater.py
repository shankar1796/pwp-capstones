class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.new_email = email
        print("This user's email has been updated")

    def __repr__(self):
        return "User: " + self.name + ", email: " + self.email + ", books read: " + str(list(self.books.values()))

    def read_book(self,book,rating):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for rating in self.books:
            total += self.books[rating]
        average = total/len(self.books)
        return average

    def __eq__(self,name_a,name_b,email_a,email_b,user_a,user_b):
        if (name_a == name_b) and (email_a == email_b):
            user_a = user_b

class Book(object):
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated")

    def add_rating(self,rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        total1 = 0
        for rating in self.ratings:
            total1 += self.ratings[rating]
        average1 = total1/len(self.ratings)
        return average1

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self,title_a,title_b,isbn_a,isbn_b,book_a,book_b):
        if (title_a == title_b) and (isbn_a == isbn_b):
            book_a = book_b


class Fiction(Book):
    def __init__(self,title,isbn,author=None):
        super().__init__(title,isbn)
        if author:
            self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title,author=self.author)

class Non_Fiction(Book):
    def __init__(self,title,isbn,subject = None,level = None):
        super().__init__(title,isbn)
        if subject:
            self.subject = subject
        if level:
            self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level,subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self,title,isbn):
        self.title = title
        self.isbn = isbn
        return Book(title,isbn)

    def create_novel(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        return Fiction(title,author,isbn)

    def create_non_fiction(self,title,subject,level,isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        return Non_Fiction(title,subject,level,isbn)

    def add_book_to_user(self,book,email,rating= None):
        if email in self.users.keys():
            user = self.users.get(email,None)
            user.read_book(book,rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}!".format(email=self.email))

    def add_user(self,name,email,user_books=None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book,email)

    def print_catalog(self):
        print(self.books.keys())

    def print_users(self):
        print(self.users.values())

    def most_read_book(self):
        max = 0
        for value in self.books.values():
            if value >= max:
                value = max
            else:
                max = max
        return value

    def highest_rated_book(self):
        max1 = 0
        for value1 in self.books.get_average_rating():
            if value1 >= max1:
                value1 = max1
            else:
                max1 = max1
        return value1

    def most_positive_user(self):
        rating_max = 0
        user_max = None
        for user in self.users.values():
            mean = User.get_average_rating(self)
            if User.get_average_rating(self) > rating_max:
                rating_max = User.get_average_rating(self)
                user_max = user
        return user_max
