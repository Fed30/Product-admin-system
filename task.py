class Product: #parent class creation
    def __init__(self,product_id,price,prime_eligible,number_in_stock,date_added): #constructor function
        self.product_id = product_id
        self.price = price
        self.prime_eligible= prime_eligible
        self.number_in_stock = number_in_stock
        self.date_added = date_added
    def set_product_id(self,value): #product_id setter
        self.product_id = value
    def get_product_id(self): #product_id getter
        return self.product_id
    def set_price(self,value): #price setter
        self.price = value
    def get_price(self): #price getter
        return self.price
    def set_prime_eligible(self,value): #prime_eligible setter
        self.prime_eligible = value
    def get_prime_eligible(self): #prime_eligible getter
        return self.prime_eligible
    def set_number_in_stock(self,value): #number_in_stock setter
        self.number_in_stock = value
    def get_number_in_stock(self): #number_in_stock getter
        return self.number_in_stock
    def set_date_added(self,value): #data_added setter
        self.date_added = value
    def get_date_added(self): #data_added getter
        return self.date_added
    def print_details(self):  # function that print the value of all data fields
        print("Product ID: ",self.product_id)
        print("Price: " ,self.price)
        print("Prime Eligible: " ,self.prime_eligible)
        print("Number in stock: ",self.number_in_stock)
        print("Date added: " ,self.date_added)
    
class book(Product): #child class creation
    def __init__(self,product_id,price,prime_eligible,number_in_stock,date_added,title,author,num_pages,pubblisher,publication_date): # contructor function
        super().__init__(product_id,price,prime_eligible,number_in_stock,date_added)
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.pubblisher = pubblisher
        self.publication_date = publication_date
    def set_title(self,value): #title setter
        self.title = value
    def get_title(self): #title getter
        return self.title
    def set_author(self,value): #author setter
        self.author = value
    def get_author(self): #author getter
        return self.author
    def set_num_pages(self,value): #num_pages setter
        self.num_pages = value
    def get_num_pages(self): #num_pages getter
        return self.num_pages
    def set_pubblisher(self,value): #pubblisher setter
        self.pubblisher = value
    def get_pubblisher(self): #pubblisher getter
        return self.pubblisher
    def set_publication_date(self,value): #publication_date setter
        self.publication_date = value
    def get_publication_date(self): #publication_date getter
        return self.publication_date
    def print_details(self):  # function that print the value of all data fields
        super().print_details()
        print("Title: ", self.title)
        print("Author: " ,self.author)
        print("Number of pages: " ,self.num_pages)
        print("Pubblisher: " ,self.pubblisher)
        print("Publication date: " ,self.publication_date)

#object creation
book1 = book( "51158","£4.64",False,"356","25/09/2021","Anxious people","Fredrik Backman",416,"Penguin","19/08/2021")
book2 = book( "89645","£5.89",True,"458","15/07/2021","A Time for Mercy","John Grishman",480,"Hodder Paperbacks","08/07/2021")
book3 = book( "15894","£8.47",False,"785","20/09/2021","How to survive family holiday","Hilary & Michael Whitehall",217,"Sphere","14/10/2021")

#calling print_details, setter and getter function on all objects

book1.set_product_id("34565")
book1.set_price("£3.67")
book1.set_prime_eligible(True)
book1.set_number_in_stock("256")
book1.set_date_added("25/08/2021")
print("Product ID has been set to: ", book1.get_product_id())
print("Product price has been set to: ", book1.get_price())
print("Product prime eligibility has been set to: ", book1.get_prime_eligible())
print("Product number in stock has been set to: ", book1.get_number_in_stock())
print("Product date added has been set to: ", book1.get_date_added())
book1.print_details()
print("\n")
book2.set_product_id("7862")
book2.set_price("£5.69")
book2.set_prime_eligible(False)
book2.set_number_in_stock("125")
book2.set_date_added("20/28/2021")
print("Product ID has been set to: ", book2.get_product_id())
print("Product price has been set to: ", book2.get_price())
print("Product prime eligibility has been set to: ", book2.get_prime_eligible())
print("Product number in stock has been set to: ", book2.get_number_in_stock())
print("Product date added has been set to: ", book2.get_date_added())
book2.print_details()
print("\n")
book3.set_product_id("2563")
book3.set_price("£14.23")
book3.set_prime_eligible(True)
book3.set_number_in_stock("320")
book3.set_date_added("25/10/2021")
print("Product ID has been set to: ", book3.get_product_id())
print("Product price has been set to: ", book3.get_price())
print("Product prime eligibility has been set to: ", book3.get_prime_eligible())
print("Product number in stock has been set to: ", book3.get_number_in_stock())
print("Product date added has been set to: ", book3.get_date_added())
book3.print_details()







