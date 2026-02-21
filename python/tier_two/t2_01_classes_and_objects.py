class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

if __name__ == "__main__":
    try:
        p = Product("Laptop", 999.99, 5)
        assert p.name == "Laptop"
        assert abs(p.price - 999.99) < 0.01
        assert p.stock == 5
        print("Verification successful")
    except AssertionError:
        print("Verification failed")
    except Exception as e:
        print(f"An error occurred: {e}")