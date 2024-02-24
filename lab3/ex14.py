#ex.14
from functions1 import recipe, solve


your_grams = input("Enter the weight in grams: ")
converted_result = recipe(your_grams)
print("Result of conversion:", converted_result)


num_heads = int(input('Enter number of heads: '))
num_legs = int(input('Enter number of legs: '))
chickens,rabbits  = solve(numheads, numlegs)
print("The number of chickens is: ", chickens)
print("The number of rabbits is: ", rabbits)
