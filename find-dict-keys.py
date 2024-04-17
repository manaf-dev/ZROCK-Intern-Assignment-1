# Program to find the keys in a dictionary

def find_keys(dict_list):
    #check if the dictionary contains keys, if not print a message
    if dict_list.keys():
        print(dict_list.keys())
    else:
        print('The dictionary is empty')




my_dict = {
    'name' : 'Deen',
    'age' : 21,
    'school' : 'aamusted',
    'programme' : 'BSc. Info. Tech. Edu.'
}

find_keys(my_dict)