"""
3. Convert Celsius to Fahrenheit
Concepts: map, lambda
📌 Task:
Convert a list of Celsius temperatures into Fahrenheit.
Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32;
"""
import random
input_list = [random.randint(10, 30) for i in range(5)]
fahrenheit_list = list(map(lambda x: (x * 9/5) + 32, input_list))
print(input_list)
print(fahrenheit_list)


# Chatgpt score - 9/10 & Improved code

import random

def celsius_to_fahrenheit(values: list[int]) -> list[float]:
    """
    Converts a list of Celsius temperatures to Fahrenheit using map() and lambda.
    """
    return list(map(lambda c: (c * 9/5) + 32, values))


if __name__ == "__main__":
    input_list = [random.randint(10, 30) for _ in range(5)]
    fahrenheit_list = celsius_to_fahrenheit(input_list)

    print(input_list)
    print(fahrenheit_list)

