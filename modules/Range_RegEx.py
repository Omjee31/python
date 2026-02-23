import re
string = "Hye I Am Omjee Singh"
print('Range',re.search(r'[a-zA-Z]',string))
print('Omjee',re.search(r'\bOmjee\b',string))
