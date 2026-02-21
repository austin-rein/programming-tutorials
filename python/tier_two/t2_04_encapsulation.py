class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid age")

if __name__ == "__main__":
    try:
        # Create product with valid price
        p = Product("Laptop", 1000)
        assert p.price == 1000
        
        # Try to set a valid new price
        p.price = 1200
        assert p.price == 1200
        assert p._price == 1200
        
        # Try to set an invalid negative price
        p.price = -500
        # The price should REMAIN 1200
        assert p.price == 1200 
        
        print("Verification successful")
    except AssertionError:
        print("Verification failed")
    except AttributeError:
        print("Attribute Error: Check your property names")
    except Exception as e:
        print(f"An error occurred: {e}")