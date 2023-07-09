class Producto:
    def __init__(self,name,price,category,description):
        self.name=name
        self.price=price
        self.category=category
        self.description=description

    def __str__(self):
        return f"{self.name} - {self.price} - {self.category} - {self.description}"