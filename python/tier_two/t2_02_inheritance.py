class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock)
        self.weight = weight

if __name__ == "__main__":
    try:
        p = PhysicalProduct("Dumbbell", 25.00, 10, 5.5)
        assert p.name == "Dumbbell"
        assert p.price == 25.00
        assert p.stock == 10
        assert p.weight == 5.5
        assert isinstance(p, Product)
        assert isinstance(p, PhysicalProduct)
        print("Verification successful")
    except AssertionError:
        print("Verification failed")
    except NameError:
        print("Class definitions missing")
    except Exception as e:
        print(f"An error occurred: {e}")
