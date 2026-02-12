str_name = 'Simon'
str_words = 'Data Analyst'
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

str_name_upper = str_name.upper()
str_name_lower = str_name.lower()
str_words_count_a = str_words.count('a')

print('String operations')
print('Original string: ' + str_name)
print('Upper case string: ' + str_name_upper)
print('Lower case string: ' + str_name_lower)
print('Count of "a" in string: ' + str(str_words_count_a))


int_1 = 5
int_2 = 10

bool_var = True
print(type(bool_var))

str_bool_var = str(bool_var)
print(type(str_bool_var))

int_bool_var = int(bool_var)
print(type(int_bool_var))


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

list_of_ratings = list(list_of_ratings) # creating a new list using the list() constructor
print('New list of ratings using list() constructor: ' + str(list_of_ratings))

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

list_rankings = [4.75, 1.38, 4.03, 3.93, 4.17, 4.23, 2.68, 1.38, 4.10, 4.20, 2.60]
max_rankings = max(list_rankings)
min_rankings = min(list_rankings)
sum_rankings = sum(list_rankings)
round_max_rankings = round(max_rankings, 1)
len_list_ranking = len(list_rankings)
power_rankings = pow(list_rankings[0], 2)
sorted_rankings = sorted(list_rankings)
reversed_rankings = sorted(list_rankings, reverse=True)


print(f'List of rankings:{list_rankings}')
print(f'Max ranking: {max_rankings}')
print(f'Min ranking: {min_rankings}')
print(f'Sum of rankings: {sum_rankings}')
print(f'Rounded max ranking: {round_max_rankings}')
print(f'Length of list of rankings: {len_list_ranking}')
print(f'Power of first ranking to the power of 2: {power_rankings}')
print(f'Sorted list of rankings: {sorted_rankings}')
print(f'Reversed list of rankings: {reversed_rankings}')


""" Functions """


def find_maximum_manually(list_of_numbers):

    max_number = 0
    for number in list_of_numbers:
        if number > max_number:
            max_number = number

    return max_number

find_maximum_manually_result = find_maximum_manually(list_rankings)
print(f'Maximum found manually: {find_maximum_manually_result}')

def find_minimum_manually(list_of_numbers):
    min_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number < min_number:
            min_number = number
    return min_number

find_minimum_manually_result = find_minimum_manually(list_rankings)
print(f'Minimum found manually: {find_minimum_manually_result}')



""" Inbuilt Methods """

list_of_ratings = ['Python', 4.7, 'Java', 1.3, 'C#', 4.0, 'PHP', 3.9, 'R', 4.1, 'SQL', 4.2, 'HTML', 2.6]
list_rankings = [4.75, 1.38, 4.03, 3.93, 4.17, 4.23, 2.68, 1.38, 4.10, 4.20, 2.60]

index_of_java  = list_of_ratings.index('Java')
print(f'Index of Java in list of ratings: {index_of_java}')

index_of_python = list_of_ratings.index('Python')
capatalised_python = list_of_ratings[index_of_python].upper()
print(f'Capatalised Python: {capatalised_python}')

count_of_1_38 = list_rankings.count(1.38)
print(f'Count of 1.38 in list of rankings: {count_of_1_38}')

list_rankings.append(4.5)
print(f'List of rankings after appending 4.5: {list_rankings}')

list_rankings.reverse()
print(f'List of rankings after reversing: {list_rankings}')



""" Packages """

# pip3 install numpy
# pip3 install pandas
# pip3 install matplotlib
# pip3 install seaborn
# pip3 install scikit-learn

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split


import math

C = 2 * 0.43 * math.pi
print(f'Value of C: {C}')

from math import pi
C = 2 * 0.43 * pi
print(f'Value of C: {C}')



""" Packages: Numpy """

import numpy as np

list_rankings = [4.75, 1.38, 4.03, 3.93, 4.17, 4.23, 2.68, 1.38, 4.10, 4.20, 2.60]

np_rankings = np.array(list_rankings)
print(f'Numpy array of rankings:{np_rankings} type: {type(np_rankings)} shape: {np_rankings.shape}')


np_rankings_offset = np_rankings * 0.95
print(f'Numpy array of rankings after offset: {np_rankings_offset}')

list_scores = [85, 90, 78, 92, 88]
np_scores = np.array(list_scores)
mean_score = np.mean(np_scores)
print(f'Mean score: {mean_score}')

np_scores_index_4 = np_scores[4]
print(f'Index 4 of numpy array of scores: {np_scores_index_4}')

print(f'Index 2 to 4 of numpy array of scores: {np_scores[2:5]}')

""" 2D Numpy Arrays """

np_2d_array = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

print(f'2D Numpy array: {np_2d_array} shape: {np_2d_array.shape}')

np_2d_array_index_1_3 = np_2d_array[1][3]
print(f'Index 1,3 of 2D numpy array: {np_2d_array_index_1_3}')

np_2d_second_column = np_2d_array[:, 1]
print(f'Second column of 2D numpy array: {np_2d_second_column}')

fifth_item_of_first_row = np_2d_array[0][4]
print(f'Fifth item of first row of 2D numpy array: {fifth_item_of_first_row}')

fifth_item_of_first_column_using_slice = np_2d_array[4:5, 0]
print(f'Fifth item of first column of 2D numpy array using slice: {fifth_item_of_first_column_using_slice}')


player_heights_inches = np.array([70, 72, 68, 75, 80, 65, 78, 74, 69])
player_weights_pounds = np.array([180, 190, 170, 210, 250, 160, 230, 220, 175])
player_ages = np.array([25, 30, 35, 28, 32, 38, 22, 27, 40])

np_player_data = np.column_stack((player_heights_inches, player_weights_pounds, player_ages))
print(f'3D Numpy array of player data: {np_player_data} shape: {np_player_data.shape}')

np_convesion = np.array([0.0254, 0.453592, 1])
np_converted_player_data = np_player_data * np_convesion
print(f'Converted player data: {np_converted_player_data} shape: {np_converted_player_data.shape}')

########## NUMPY ARRAY OPERATIONS ##########


np_height = np_player_data[:, 0]
np_weight = np_player_data[:, 1]
np_age = np_player_data[:, 2]

np_mean_height = np.mean(np_height)
print(f'Mean height: {np_mean_height}')

np_median_weight = np.median(np_weight)
print(f'Median weight: {np_median_weight}')

np_player_data = [[70, 180, 25],
                  [72, 190, 30],
                  [68, 170, 35],
                  [75, 210, 28],
                  [80, 250, 32],
                  [65, 160, 38],
                  [78, 230, 22],
                  [74,220, 27],
                  [69, 175, 40]]

np_player_data_array = np.array(np_player_data)
np_player_data_updates = np_player_data_array * np.array([0.0254, 0.453592, 1])
print(f'Updated player data array: {np_player_data_updates} shape: {np_player_data_updates.shape}')


# Calculate height (col 1 is [:, 0]) overview

mean_height = np.mean(np_player_data_updates[:, 0])
max_height = np.max(np_player_data_updates[:, 0])
min_height = np.min(np_player_data_updates[:, 0])
std_dev_height = np.std(np_player_data_updates[:, 0])
median_height = np.median(np_player_data_updates[:, 0])
correlation_height = np.corrcoef(np_player_data_updates[:, 0], np_player_data_updates[:, 1])

print(f'Mean height: {mean_height}')
print(f'Max height: {max_height}')
print(f'Min height: {min_height}')
print(f'Standard deviation of height: {std_dev_height}')
print(f'Median height: {median_height}')
print(f'Correlation between height and weight: {correlation_height}')



""" Matplotlib """
# pip3 install matplotlib
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2020]
population = [2.519, 3.692, 5.263, 6.972, 7.794]

plt.plot(year, population)
plt.title('World population growth')
plt.xlabel('Year')
plt.ylabel('Population (billions)')
plt.show()


plt.scatter(year, population)
plt.title('World population growth | Scatter plot')
plt.xlabel('Year')
plt.ylabel('Population (billions)')
plt.show()



