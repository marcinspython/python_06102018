import json

employees_list = []
print(type(employees_list))
employees_list = ["Adam", "Nowak", "1980", "5000"]
print(type(employees_list))
print(employees_list)

employees_list_as_json = json.dumps(employees_list)
print(employees_list_as_json)

read_employees_from_json = json.loads(employees_list_as_json)
print(read_employees_from_json)

with open("employees.json", "w") as f:
    json.dump(employees_list, f)
    print(employees_list)

with open("employees.json") as f:
    employees_list = json.load(f)
    print(employees_list)

with open("employees.json") as f:
    employees_list = json.load(f)
    employees_list.append("NEW")
    print(employees_list)

print(employees_list)
with open("employees.json", "w") as f:
    json.dump(employees_list, f)

# print("Co chcesz zrobić: ?")
# print(input("Imię: "))
# print(input("Nazwisko: "))
# print(input("Rok urodzenia: "))
# print(int(input("Pensja: ")))
