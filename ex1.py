# Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes. Create a print_information method to both subclasses
# for printing out all information of the publication in question. In the main program, create publications
# Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all
# information of both publications using the methods you implemented.

class publication:
    def __init__(self,name):
        self.name=name


    def print_info(self):
        print(f"Name of publication is : {self.name}")


class magazine(publication):
    def __init__(self,name,editor):
        self.editor=editor
        super().__init__(name)
    def print_info(self):
        super().print_info()
        print(f"Editor is {self.editor}")


class book(publication):
    def __init__(self,name,author,page_count):
        self.author=author
        self.page_count=page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Author is: {self.author} amount of page is :{self.page_count}")

publication=[]
publication.append(magazine("donald duck","aki hyyppa"))
publication.append(book("No 6","rosa liksom",192))
for i in publication:
    i.print_info()
