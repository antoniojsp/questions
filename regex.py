import re

txt = "The rain in Spain"
x = re.findall("i", txt)
print(len(x))