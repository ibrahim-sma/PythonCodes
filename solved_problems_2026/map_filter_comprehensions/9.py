"""
9. Apply Discount to Prices
Concepts: map, lambda
📌 Task:
Given a list of product prices, apply a 20% discount and return final prices.
"""

input_price_list = [100, 320, 414, 288, 324]
discounted_list = list(map(lambda x: x * 0.8, input_price_list))
print(discounted_list)


# chatgpt Score 9/10 and optimized code
def apply_discount(prices: list[float]) -> list[float]:
    """
    Applies a 20% discount to each price using map and lambda.
    """
    return list(map(lambda p: round(p * 0.8, 2), prices))


if __name__ == "__main__":
    input_price_list = [100, 320, 414, 288, 324]
    print(apply_discount(input_price_list))