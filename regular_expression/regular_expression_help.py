# %%
import re

# %%
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900.555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# %%

# compile a pattern so that it can be used multiple times
pattern = re.compile(r'abc')  # search is case sensitive
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
print(text_to_search[1:4])

# %%
# if you want to search for special characters you have to use \
pattern = re.compile(r'coreyms\.com')  # search is case sensitive
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%
pattern = re.compile(r'\D')  # it will match for not a digit
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%
pattern = re.compile(r'\D')  # it will match for not a digit
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
# %%
pattern = re.compile(r'\bHa')  # it will match for not a digit
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
# %%
pattern = re.compile(r'^Start')  # it will match for not a digit
matches = pattern.finditer(sentence)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%
pattern = re.compile(r'end$')  # it will match for not a digit
matches = pattern.finditer(sentence)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
# %%

# matching a phone number
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')  # it will match for not a digit
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%
# reading data.txt file
with open('regular_expression/data.txt', 'r') as file:
    data = file.read()

# %%
pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')  # here \ is not required at the beginning of . to match . here it will
# search for . not for any character
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%
# if we only want to match 800 or 900 number

pattern = re.compile(
    r'[89]00[-.]\d{3}[-.]\d{4}')  # here \ is not required at the beginning of . to match . here it will
# search for . not for any character
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%

# if we want to search number between 1 to 5

pattern = re.compile(r'[1-5]')  # here \ is not required at the beginning of . to match . here it will
# search for . not for any character
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
# %%

pattern = re.compile(r'[a-zA-Z]')  # here \ is not required at the beginning of . to match . here it will
# search for . not for any character
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

pattern = re.compile(
    r'[^a-zA-Z]')  # here we have put ^ at the beginning of char set so it will search for anything that
# is not in the charset
# %%
# if you want to search for cat mat pat but not bat
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
# %%
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  # look for names starting with Mr
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)

# %%

# if we want to match Mr. and Ms in text to search with name we can use group for easy reading code

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # () will create grouping with | sign it will search for either r or s
# or rs
matches = pattern.finditer(text_to_search)  # it will return iter function with give details about span and match
for match in matches:
    print(match)
