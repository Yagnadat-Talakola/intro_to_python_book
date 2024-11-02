# 1. Concatenate two strings with your first and last name, to create
# a new string with your full name as its value

first_name = 'Yagnadat'
last_name = 'Talakola'
full_name = first_name + ' ' + last_name
print(full_name)

# 2. Use the REPL and the arithmetic operators to extract 
# individual digits of 4936

input_num = str(4936)
ones_place = input_num[-1]
tens_place = input_num[-2]
hundreds_place = input_num[-3]
thousands_place = input_num[-4]

print(f'''ones place: {ones_place}, 
    tens place: {tens_place}, 
    hundreds place: {hundreds_place},
    and thousands place: {thousands_place}''')

# 3. What does the following code do and why?

print('5' + '10') # this will first concatenate the two strings and then print the result

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead

print(int('5') + int('10'))

# 5. Will an error occur if you try to access a list element with an index
# greater than or equal to the list's length

foo = ['a', 'b', 'c']
# print(foo[3])      # will this result in an error?
# this will result in error as we're trying to access element of an index that does not exist

# 6. To what value does the following expression evaluate?

'foo' == 'Foo' # False; f and F have different unicode representation

# 7. what will the following code do and why?

# int('3.1415') # this is explicit coercion of a string to int type
# this will result in a error as the string we want to coerce is not coercable to int
# int('3') can be coerced to int type as 3 is a integer but 3.1415 is float type
# float('3.1415) should work

print(float('3.1415'))

# 8. to what value does the following expression evaluate?

print('12' < '9') # due to character by character comparision starting from left to right
# '1' is compared to '9' and the result is True for '1' < '9'