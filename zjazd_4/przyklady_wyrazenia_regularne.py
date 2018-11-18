import re

patter = re.compile("\d{3}")

text = "123"

print(patter.findall(text))
