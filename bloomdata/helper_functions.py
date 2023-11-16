import pandas as pd
import numpy as np

# Write a function that can create a random combination of adjectives and nouns. When called the 
# function should return a single string containing a randomly selected adjective and noun pair:
# Adjectives: ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
# nouns: ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
adjective_list = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
noun_list = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2 ):
    
    item1 = np.random.choice(adjective_list, size = None, replace=True)
    item2 = np.random.choice(noun_list, size = None, replace=True)
    #print(word_1,word_2)
    return str(item1) + ' ' + str(item2)
 

if __name__ == '__main__':
    print(random_phrase(adjective_list, noun_list))

# def random_float(min_val, max_val):
#     #print(np.random.uniform(min_val, max_val))
#     return (np.random.uniform(min_val, max_val))

# # df = pd.DataFrame({'a':[1,2,3] , 'b': [4,5,6]})

# # print(df.head())

# print(random_float(3.3,8.5))

# def random_bowling_score():
#     return(np.random.randint(0,300))
# print(random_bowling_score())

# def silly_tuple():
#     phrase1,phrase2 = random_phrase()
#     rating = random_float(1,5)
#     score = random_bowling_score()
#     return(phrase1,phrase2,rating,score)
    

# phrase1,phrase2,rating,score = silly_tuple()
# print(phrase1,phrase2,rating,score)

# def silly_tuple_list(num_tuples):
#     tuple_list = []
#     for i in range(num_tuples):
#         tuple_list.append(silly_tuple())
#     return tuple_list

# tuple_list = silly_tuple_list(3)
# print(tuple_list)

# def null_count(df):
#     count = 0
#     #print(df)
#     for row in df.itertuples(index=False, name='Pandas'):
#         row_list = (np.asarray(row))
#         for item in row_list:
#             if item == 'NaN':
#                 count +=1
#     return count
    
    

# df = pd.DataFrame({'column 0':['NaN',4,3] , 'column 1': [9,'NaN','NaN'] , 'column2' : [10,2,2]})

# count = null_count(df)
# print(count)
