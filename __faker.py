from faker import Faker
import random

fake = Faker()

print("----------Names-------------\n")
for _ in range(10):
    name = fake.name()
    print(name)
print("-----------------------------\n")

print("----------Passwords-------------\n")
for _ in range(10):
    password = fake.password()
    print(password)
print("-----------------------------\n")

print("----------Date-of-birth-------------\n")
for _ in range(10):
    date = fake.date_of_birth()
    print(date)
print("-----------------------------\n")

print("----------Email-------------\n")
for _ in range(10):
    email = fake.email()
    print(email)
print("-----------------------------\n")

# print("----------Phones-------------\n")
# for _ in range(10):
#     phone = fake.phone()
#     print(phone)
# print("-----------------------------\n")

print("----------Country-------------\n")
for _ in range(10):
    country = fake.country()
    print(country)
print("-----------------------------\n")
