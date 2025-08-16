import random 

# returns a random floating point number between 0.0 <= x < 1.0
random_number_0_to_2 = random.random() * 10

print(random_number_0_to_2) 

# returns a random floating point number N such as a <= N <= b or a <= b and <= N <= b for b < a
random_float_10_to_20 = random.uniform(10, 20)

print(random_float_10_to_20)