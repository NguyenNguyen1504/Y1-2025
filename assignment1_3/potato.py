print('We have 100 kg of potatoes that are 99% water. Now we dehydrate the potatoes.')
new_content = int(input('What is the new water content? (%)\n'))
percentage_of_solids = (100 - new_content) / 100
new_weight = 1 / percentage_of_solids
print(f'The new weight of the potatoes is {new_weight} kg.')