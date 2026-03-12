data = [("apple", 5), ("kiwi", 12), ("mango", 8)]
# List of tuples containing (item, quantity)

sorted_data = sorted(data, key=lambda x: x[1] % 3)
# lambda x: x[1] % 3)
# Defines an anonymous function taking tuple 'x'
# Accesses index 1 (quantity) and performs modulo 3

filtered_gen = (x for x in data if (lambda y: y > 10)(x[1]))
# (lambda y: y > 10) (x[1])
# Defines a lambda to check if quantity is > 10
# Immediately executes it passing x[1] as argument 'y'
# This reifies Hash 08 within a Hash 03 generator context

result = list(filtered_gen)
# Triggers the iteration protocol (Hash 04)
# Consumes the generator and returns a list