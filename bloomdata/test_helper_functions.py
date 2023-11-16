import bloomdata.helper_functions as hf

adjective_list = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
noun_list = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

list1 = [3,5,6]
list2  = [4.5,8.3,2]

def test_random_phrase():
    #assert isinstance(hf.random_phrase(adjective_list,noun_list),str) 
    assert isinstance(hf.random_phrase(list1,list2) , str)
