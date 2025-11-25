# Write a Python program to search for a word in a string using re.search().
# import re

# text = "Python is a powerful programming language"
# word = "powerful"

# result = re.search(word, text)

# if result:
#     print("Word found!")
# else:
#     print("Word not found!")

# Write a Python program to match a word in a string using re.match().

# import re

# text = "Hello world, welcome to Python"
# word = "Hello"

# result = re.match(word, text)

# if result:
#     print("Word matched!")
# else:
#     print("Word not matched!")

# Write a Python program to search for a word in a string using
# re.search().

# import re

# text = "Python programming is very interesting"
# word = "programming"

# result = re.search(word, text)

# if result:
#     print("Word found!")
# else:
#     print("Word not found!")

# Write a Python program to match a word in a string using re.match().
import re

text = "Python is amazing"
word = "Python"

result = re.match(word, text)

if result:
    print("Word matched!")
else:
    print("Word not matched!")            