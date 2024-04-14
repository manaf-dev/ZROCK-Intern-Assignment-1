# Program to find the index of an element in a list

def find_index(list, element):
    index = list.index(element)
    print(f'The index of \'{element}\' in the list is {index}')

your_list = ['Saeed', 'Moses', 'John', 'Ali', 'Issac', 'Deen']
element_to_find = 'Deen'
find_index(your_list, element_to_find)
