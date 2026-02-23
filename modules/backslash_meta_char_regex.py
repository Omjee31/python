import re
s = 'omjee singh is a good boy'
#without'\'
match = re.search(r'.',s)
print(match)
# with'\'
match = re.search(r'\.',s)
print(match)
