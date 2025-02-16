class Product ():
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display_info(self):
        print (f"Ime proizvoda:{self.name}")
        print (f"Cena proizvoda:{self.price}")
        print (f"Kolicina proizvoda:{self.quantity}")
    def update_quantity(self,new_quantity):
        self.quantity=new_quantity
        print (f"Kolicina je azurirana na {self.quantity} komada")
p1=Product("coko",150,20)

        