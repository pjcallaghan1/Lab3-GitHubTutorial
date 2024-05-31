# Author: CSC 221 Instructor
# Date: January 2023
# Description: Simple Shelter program for IDLE portion of Lab

# Shelter capacity values
DOG_CAP = 25
CAT_CAP = 50

# Gather shelter animal input - INTEGER VALUES REQUIRED
num_dogs = int(input('Enter number of dogs in the shelter: '))
num_cats = int(input('Enter number of cats in the shelter: '))

# Calculate percent of shelter capacity values
dog_percap = num_dogs/DOG_CAP * 100
if dog_percap > 100:
    print(f'DOG MAX={str(num_dogs)}: CRISIS SITUATION - shelter at %{dog_percap:.2f} of dog capacity')
else:
    print(f'DOG MAX={str(num_dogs)}: Shelter at %{dog_percap:.2f} of dog capacity')

cat_percap = num_cats/CAT_CAP * 100
if cat_percap > 100:
    print(f'CAT MAX={str(num_cats)}: CRISIS SITUATION - shelter at %{cat_percap:.2f} of cat capacity')
else:
    print(f'CAT MAX={str(num_cats)}: Shelter at %{cat_percap:.2f} of cat capacity')

# Calculate total number of animals at the shelter
total = num_dogs + num_cats
print(f'TOTAL shelter population is {str(total)} animals')
