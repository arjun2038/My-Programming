#Create a class Publisher (name). Derive class Book from Publisher with attributes title and 
#author. Derive class Python from Book with attributes price and no_of_pages. Write a 
#program that displays information about a Python book. Use base class constructor invocation and 
#method overriding.
class Publisher:
    "Information about books"
    def __init__(self,pubname):
        self.pubname=pubname
    def display(self):
         print("Publisher Name:", self.pubname)


         
class Book(Publisher):
     def __init__(self,pubname,title,author):
         Publisher.__init__(self,pubname)
         self.title=title
         self.author=author

     def display(self):
          print("Title: ",self.title)
          print("Author: ",self.author)

          
class Python(Book):
     def __init__(self,pubname,title,author,price,no_of_pages):
        Book.__init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
     def display(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Price: ",self.price)
        print("Number of pages: ", self.no_of_pages)
           
s1=Python("ak books","Taming Python By Programming  ",' Jeeva Jose  ' ,200,219)
s1.display()