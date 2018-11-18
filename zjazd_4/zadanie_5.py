# w input.txt znajdź wszystkie wytąpienia:
# kodów pocztowych: 12-123
# adresów email: test@email.com
# dat: 12 Jan 1990
# Skorzystaj z modułu re.

import re
line = "why people don't know what regex are? let me know asdfal2@als.com, Users1@gmail.de " \
       "Dariush@dasd-asasdsa.com.lo,Dariush.lastName@someDomain.com"
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
for i in match:
    print(i)

# [\w\.-]+@[\w\.-]+

file = open(“dane/input.txt”,”r”)
print(file)

