# Code your solution here
word = input()
rev_word = word[::-1]
if word == rev_word:
    is_palindrome = True
else:
    is_palindrome = False