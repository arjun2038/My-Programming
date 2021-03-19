class Publisher:
    def __init__(self, Pubname):
        self.Pubname = Pubname

    def display(self):
        print("Publisher name is:", self.Pubname)


class Book(Publisher):
    def __init__(self, Pubname, title, author):
        Publisher.__init__(self, Pubname)
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, Pubname, title, author, price, no_of_pages):
        Book.__init__(self, Pubname, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("No of pages:", self.no_of_pages)


ob1 = Python("New coders", "Who Am I?", "R P N Singh ", 1000, 1944)
ob1.display()
