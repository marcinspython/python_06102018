# w input.txt znajdź wszystkie wytąpienia:
# kodów pocztowych: 12-123
# adresów email: test@email.com
# dat: 12 Jan 1990
# Skorzystaj z modułu re.

import re

POST_CODE_PATTERN = re.compile("^\d{2}-\d{3} | ^\d{2}-\d{3} | ^\d{2}-\d{3}$")
EMAIL_PATTERN =
DATE_PATTERN = 

with open("input.txt") as f:
    data = f.read()
    print(POST_CODE_PATTERN.findall(data))

