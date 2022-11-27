import re
from my_input import my_input2


# str -> dict[str, str]
# description: headers from Burp
# result = dict(my_input2(
#     execute_with_element=lambda row: re.split(': ', row)))


# str -> dict[str, str]
# descripions: cookies from Burp
# result = dict(my_input2(
#     inside_string=lambda row: re.split("; ", row),
#     execute_with_element=lambda row: re.split('=', row)))
