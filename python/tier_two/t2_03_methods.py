class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent):
        self.price = (self.price - ((self.price * percent) / 100))
    
    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock = self.stock - quantity
            return True
        else:
            return False
        


if __name__ == "__main__":
    try:
        item = Product("Headphones", 100.0, 10)
        
        item.apply_discount(20)
        assert abs(item.price - 80.0) < 0.001
        
        success = item.sell(3)
        assert success is True
        assert item.stock == 7
        
        fail = item.sell(10)
        assert fail is False
        assert item.stock == 7
        
        print("Verification successful")
    except AssertionError:
        print("Verification failed")
    except Exception as e:
        print(f"An error occurred: {e}")