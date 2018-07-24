# Dan B Tome_Rater

class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('{}s email address has been updated'.format(self.name))
    
    def __repr__(self):
        return 'User {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books))

    def __eq__(self, other):
        if (self.name == other.name) and (self.email == other.email):
            return True
        else:
            return False
        
    def read_book(self, book, rating = None):
        self.books[book] = rating
        
    def get_average_rating(self):
        sum_rating = 0
        number_of_books = 0
        for rating in self.books.values():
            if rating:
                sum_rating += rating
                number_of_books += 1
        return sum_rating / number_of_books


            
class Books:
    
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('Title: {} has been updated with a new isbn: {}.'.format(self.title, self.isbn))
        
    def add_rating(self, rating):
        if rating  and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating')
            
    def __eq__(self, other):
        
        if (self.title == other.title) and (self.isbn == other.isbn):
            return True
        else:
            return False
        
    def get_average_rating(self):
        rating_sum = 0
        average_rating = 0
        for value in self.ratings:
            rating_sum += value
        if rating_sum == 0:
            average_rating = 0
        else:
            average_rating = rating_sum / len(self.ratings)
        return average_rating
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        return '{} isbn {} price {}'.format(self.title, self.isbn, self.price)
        

class Fiction(Books):
    
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return '{} by {} price {}'.format(self.title, self.author, self.price)
    
        
class Non_Fiction(Books):
    
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return '{}, a {} manual on {} price {}'.format(self.title, self.level, self.subject, self.price)
    
    
class TomeRater:
    
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn, price):
        book = Books(title, isbn, price)
        return book
    
    def create_novel(self, title, author, isbn, price):
        fiction = Fiction(title, author, isbn, price)
        return fiction
    
    def create_non_fiction(self, title, subject, level, isbn, price):
        non_fiction = Non_Fiction(title, subject, level, isbn, price)
        return non_fiction
    
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print('No user with email {}!'.format(self.email))
            
            
    def add_user(self, name, email, user_books = None):
        user = User(name, email)
        self.users[email] = user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
                
                
# Analysis
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
        
    def print_users(self):
        for user in self.users.keys():
            print(user)
            
    def most_read_book(self):
        most_read_book = ""
        count = 0
        for book in self.books.keys():
            if self.books[book] > count:
                count = self.books[book]
                most_read_book = book
        return most_read_book
    
    def highest_rated_book(self):
        highest_book = ""
        highest_avg = 0
        for book in self.books.keys():
            if highest_avg < book.get_average_rating():
                highest_avg = book.get_average_rating()
                highest_book = book.title
        return highest_book
    
    def most_positive_user(self):
        highest_avg = 0
        highest_user = ""
        for user in self.users.values():
            user_average = user.get_average_rating()
            if user_average > highest_avg:
                highest_avg = user_average
                highest_user = user.name
        return highest_user

    # gets the most expensive book
    def get_most_expensive_book(self):
        most_expensive = ""
        price = 0
        for book in self.books.keys():
            if book.price > price:
                price = book.price
                most_expensive = book.title
        return [most_expensive, price]

    # gets the most expensive books at or over n     
    def get_n_most_expensive_books(self, n):
        most_expensive = {}
        for book in self.books.keys():
            if book.price >= n:
                most_expensive[book] = book.price
        return most_expensive
   
    # gets the cheapest books at or below n
    def get_n_cheapest_books(self, n):
        least_expensive = {}
        for book in self.books.keys():
            if book.price <= n:
                least_expensive[book] = book.price
        return least_expensive
  
    # gets the value of users read books      
    def get_worth_of_user(self, user_email):
        value_read_books = 0
        if user_email in self.users.keys():
            for book in self.users[user_email].books:
                value_read_books += book.price
        return value_read_books
    
                
            
       
      
            
        
            
    
    
    
    
        
            
            

        



        
    
    


#print('{}s email address has been changed'.format('test'))

#print('test')
