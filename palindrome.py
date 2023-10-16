#Write a program to indentify if a string is a palindrome or not
def is_Palindrome(word):
    word_array = [char for char in word]
    return word_array == word_array[::-1]

word = str(input("Write a word "))

if is_Palindrome(word):
    print(word,"is a palindrome")

else:
    print(word," is not a palindrome")

