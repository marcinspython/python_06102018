# python clean_emails.py emails.txt cleaned_emails.txt
import sys


def validate_email(line):
    line = line.strip().lower()
    if line.count('@') == 1:
        return line


if len(sys.argv) == 3:  # równa 3 parametry
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()
    with open(input_file) as f:
        for line in f:
            email = validate_emil(line)
            if email:
                emails.add(email)

    with open(output_file, 'w') as f:
        for email in sorted(emails):
            f.write(email + "\n")
else:
    print("nieprawidlowa ilosc parametrów")

# python files_zad3.py dane\emails.txt cvlean_emails.txt RUN!!!!!!!!!!! in command line
# powinno uporzadkowac maile i zapisac p w pliku clean....