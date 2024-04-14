#program that finds substring in a string

def find_substring(string, substring):
    index = string.find(substring)
    print(f'The index of the substring is {index}')

text = input('Enter the text: ')
text_to_find = input('Enter the text to find: ')

find_substring(text, text_to_find)