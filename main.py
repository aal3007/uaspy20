class MainApp():
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()

class InputBook():
    def input(self):
        print("========================================")
        print("|              Add Book                |")
        print("========================================")
        title  = input("Title  : ")
        author = input("Author : ")
        price  = input("Price  : ")
        copies = input("Copies : ")
        price = float(price) if price.isnumeric() else 0
        copies = int(price) if copies.isnumeric() else 0
        return Book(title, Author(author), price, copies)

    def search(self):
        print("========================================")
        print("|            Search Book               |")
        print("========================================")
        key = input("Title : ")
