# ex1
import re
#file = open(fr'C:\Users\user\Desktop\Python_II\TSIS5\row.txt', 'r', encoding='utf-8')
x=input()
y=re.match(r'a(b*)+',x)
print(y)
# ex2
import re
x=input()
y=re.match("a{1}b{2,3}", x)
print(y)
# ex3
import re
x=input()
y=re.findall(r'([a-z]+_[a-z]+)', x)
print(y)
# ex4
import re
x=input()
y=re.findall(r'[A-Z][a-z]+',x)
print(y)
# ex5
import re
x=input()
y=re.match(r'a.*b$',x)
print(y)
# ex6
import re
x=input()
y=re.sub(r'[\s,.]',r':',x)
print(y)
# ex7
import re

def snake_to_camel(snake_str):
    # Use regular expression to replace underscore followed by a lowercase letter with
    # the uppercase version of the letter
    camel_case_str = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)
    return camel_case_str

# Example usage
snake_case_string = "this_is_a_snake_case_string"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)
# ex8
import re
x=input()
y=re.split(r'[A-Z]', x)
print(y)
# ex9
import re
x=input()
y=re.compile('(?=[A-Z])')
z=y.sub(' ', x)
print(z)
# ex10
import re

def camel_to_snake(camel_str):
    # Insert an underscore before any uppercase letters in the string and convert it to lowercase
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_case_str

# Example usage
camel_case_string = "ThisIsACamelCaseString"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case string:", camel_case_string)
print("Snake case string:", snake_case_string)