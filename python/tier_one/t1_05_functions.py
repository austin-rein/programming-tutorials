def calculate_total(base_price, *taxes, **discounts):
    current_total = base_price

    for tax in taxes:
        current_total += (base_price * tax)
    
    for discount in discounts:
        current_total -= float(discounts[discount])
    
    return current_total

print(f"Final Total: ${calculate_total(100.0, 0.05, 0.03, special_offer=10)}")