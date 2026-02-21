class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processed Credit Card payment of ${amount}"
    
class PayPalPayment:
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}"


def checkout(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    try:
        cc = CreditCardPayment()
        pp = PayPalPayment()
        
        # Verify the methods return the correct strings
        assert cc.process_payment(100) == "Processed Credit Card payment of $100"
        assert pp.process_payment(50.5) == "Processed PayPal payment of $50.5"
        
        # To test the checkout function, we can't easily assert print statements,
        # but we can verify it runs without crashing on both types.
        checkout(cc, 100)
        checkout(pp, 50.5)
        
        print("Verification successful")
    except AssertionError:
        print("Verification failed: Return strings do not match requirements")
    except AttributeError:    
        print("Verification failed: Missing method 'process_payment'")
    except Exception as e:
        print(f"An error occurred: {e}")