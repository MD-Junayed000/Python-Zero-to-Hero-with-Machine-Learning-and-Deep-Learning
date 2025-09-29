# MAgic Method = Dunder MEthod __init__, __str__, __eq__

class Book:
    def __init__(self,author,book,pages):
        self.author=author
        self.book=book
        self.pages=pages

    def display(self):
        return f'{self.author} by {self.book}'

    def __lt__(self,other): ## lt == less than
        return self.pages<other.pages

    def __add__(self,other):
        return f'{self.pages+other.pages} pages'


    def __getitem__(self,key):
        if key=='title':
            return self.book

book1= Book('Junayed','The Hawkins',245)
book2=Book('Yeasmin Wiynaldum','The FUcks',678)

print(book2.display())
print(book1==book2)
print(book1<book2) ###### pages

## total pages
print(book1+book2)

## book name
print(book2['title'])