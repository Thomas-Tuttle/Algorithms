#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    total_batches = -1
    for i in recipe:
        if i in ingredients:
            if ingredients[i] // recipe[i] < total_batches or total_batches == -1:
                total_batches = ingredients[i] // recipe[i]
        else:
            return 0
    return total_batches 


test_recipe = { 'Cream Cheese': 8, 'Chicken Broth': 0.33, 'Ranch': 0.33, 'Buffalo Sauce': 8 }
test_ingredients = { 'Cream Cheese': 35, 'Chicken Broth': 7, 'Ranch': 10, 'Buffalo Sauce': 50 } 
x = recipe_batches(test_recipe, test_ingredients)
print(f'You can make', x, 'batches')

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))