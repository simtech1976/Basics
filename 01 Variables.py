str_name = 'Simon'
int_age = 49
float_height = 5.10
bool_human = True
list_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

""" Math operations with variables """

addition = 5 + 4
subtraction = 5 - 4
multiplication = 5 * 4
division = 5 / 4
floor_division = 5 // 4
modulus = 5 % 4
exponentiation = 5 ** 4

print('-' * 50)
print('Basic math operations')
print('-' * 50)
print('Addition:' + str(addition))
print('Subtraction:' + str(subtraction))
print('Multiplication:' + str(multiplication))
print('Division:' + str(division))
print('Floor Division:' + str(floor_division))
print('Modulus:' + str(modulus))
print('Exponentiation:' + str(exponentiation))
print('_' * 50)

int_1 = 5
int_2 = 10


weight1 = 150.5
weight2 = 200.5
weight3 = 250.9
weight4 = 312.5

list_weights = [weight1, weight2, weight3, weight4]
print('List of weights: ' + str(list_weights))

list_weights_with_info = ['item1: ' + str(weight1), 'item2: ' + str(weight2), 'item3: ' + str(weight3), 'item4: ' + str(weight4)]
print(list_weights_with_info)
print('List of weights with info: ' + str(list_weights_with_info))
print('second item of list of lists: ' + str(list_weights_with_info[1]))
print('last item of list of lists: ' + str(list_weights_with_info[-1]))
print('first 2 items of list of lists: ' + str(list_weights_with_info[0:2]))

last_two_items = list_weights_with_info[-2:]
print('last 2 items of list of lists: ' + str(last_two_items))

first_two_items = list_weights_with_info[:2]
print('first 2 items of list of lists: ' + str(first_two_items))

slice_of_items = list_weights_with_info[2:5]
print('slice of items from index 2 to 4: ' + str(slice_of_items))


list_of_lists = [['item1', weight1], ['item2', weight2], ['item3', weight3], ['item4', weight4]]
print('List of lists: ' + str(list_of_lists))


subset_of_list_of_lists = list_of_lists[1:3]
print('Subset of list of lists: ' + str(subset_of_list_of_lists))
subset_to_select_last_item_of_2nd_list = list_of_lists[1][1]
print('Last item of 2nd list in subset: ' + str(subset_to_select_last_item_of_2nd_list))



""" Manipulating Lists"""
print('Manipulating Lists')
print('-' * 50)
print('Amending a list')

list_of_ratings = ['Python', 4.7, 'Java', 1.3, 'C#', 4.0, 'PHP', 3.9, 'R', 4.1, 'SQL', 4.2, 'HTML', 2.6]
print('Original list of ratings: ' + str(list_of_ratings))

list_of_ratings_copy = list_of_ratings[:]
print('Copy of list of ratings: ' + str(list_of_ratings_copy))

list_of_ratings_copy[1] = 4.8
print('Amended copy of list of ratings: ' + str(list_of_ratings_copy))

list_of_ratings_copy[12] = 'HTML/CSS'
print('Amended copy of list of ratings: ' + str(list_of_ratings_copy))

list_of_ratings_copy[-1] = 1.8 # negative indexing to amend last item of list
print('Amended copy of list of ratings: ' + str(list_of_ratings_copy))

list_of_ratings_copy = list_of_ratings_copy + ['Javascript', 2.4] # adding items to list using concatenation
print('Amended copy of list of ratings: ' + str(list_of_ratings_copy))

del list_of_ratings_copy[14:16] # deleting item from list using del keyword
print('Amended copy of list of ratings: ' + str(list_of_ratings_copy))

reference_to_list_of_ratings = list_of_ratings
print('Reference to list of ratings: ' + str(reference_to_list_of_ratings) + ' (this is a reference to the original list, not a copy)')


""" Built in Functions """
print('\nBuilt in Functions')
print('-' * 50)

list_rankings = [4.75, 1.38, 4.03, 3.93, 4.17, 4.23, 2.68]
max_rankings = max(list_rankings)
min_rankings = min(list_rankings)
sum_rankings = sum(list_rankings)
round_max_rankings = round(max_rankings, 1)

print(f'List of rankings:{list_rankings}')
print(f'Max ranking: {max_rankings}')
print(f'Min ranking: {min_rankings}')
print(f'Sum of rankings: {sum_rankings}')
print(f'Rounded max ranking: {round_max_rankings}')



