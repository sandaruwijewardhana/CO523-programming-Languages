from functools import reduce

# Input Data
products = [
    {"name": "Laptop", "category": "Electronics", "price": 1000},
    {"name": "Shirt", "category": "Clothing", "price": 50},
    {"name": "Phone", "category": "Electronics", "price": 500},
    {"name": "Book", "category": "Media", "price": 20},
    {"name": "Monitor", "category": "Electronics", "price": 300}
]

# 1. Select only Electronics
electronics = list(filter(lambda p: p["category"] == "Electronics", products))

# 2. Apply 10% discoun
discounted_prices = list(map(lambda p: p["price"] * 0.9, electronics))

# 3. Calculate total cost 
total_cost = reduce(lambda x, y: x + y, discounted_prices)

# 4. Recursive function to find the highest price
def find_highest_price(product_list):
    # Base case: only one product left
    if len(product_list) == 1:
        return product_list[0]["price"]
    
    # Recursive case- compare current head with max of the rest
    first_price = product_list[0]["price"]
    remaining_max = find_highest_price(product_list[1:])
    
    return first_price if first_price > remaining_max else remaining_max

# Verification
if __name__ == "__main__":
    print(f"Total Cost of Discounted Electronics: {total_cost}") # Output- 1620.0
    print(f"Highest Price in original list: {find_highest_price(products)}") # Output- 1000