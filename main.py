from email import message
import random
import string
from random import randrange
from random import randint
import names
from sympy import limit


def direction():
    print("Hello, tester")
    message = int(input(
        "Привет, нажмите 1 или 2, что-бы перейти в магистратуру или бакалавр соответственно ->  "))
    if message == 1:
        magistr()
    elif message == 2:
        bacalavr()
    else:
        print("ERROR")


def magistr():
    file_1 = open("Magistratura_kurs", 'r')
    subjects1 = []
    subjects1 = file_1.read().splitlines()
    for i, subjects1 in enumerate(subjects1):
        print(i+1, subjects1)
    file_1.close()
    kurs_number = int(input("Enter your course in numbers (1,2)-> "))


def bacalavr():
    file_2 = open("Bacalavriat_kurs", 'r')
    subjects2 = []
    subjects2 = file_2.read().splitlines()
    for i, subjects2 in enumerate(subjects2):
        print(i+1, subjects2)
    file_2.close()
    kurs_number = int(input("Enter your course in numbers (1,2,3,4)-> "))
    bacalavr_level(kurs_number)


def first_kurs(kurs):
    print(f"You have chosen the {kurs} course")
    group_quantity = int(
        input(f"How many groups are there in the {kurs} year? "))
    generate_random_groups_bacalavr_first(group_quantity)
    print("Find your group in this list: ")
    groups1 = []
    file = open('First_kurs', 'r')
    groups1 = file.read().splitlines()
    for i, groups1 in enumerate(groups1):
        print(i+1, groups1)
    mes1 = int(input("Enter your group: "))
    file.close()
    with open('First_kurs') as f:
        lines = f.readlines()
        print(lines[mes1-1])
    f = open('New_Group', 'r+')
    f.write("Groups name: ")
    f.write(lines[mes1-1])
    f.close()
    create_people()


def second_kurs(kurs):
    print(f"You have chosen the {kurs} course")
    group_quantity = int(
        input(f"How many groups are there in the {kurs} year? "))
    generate_random_groups_bacalavr_second(group_quantity)
    print("Find your group in this list: ")
    groups2 = []
    file = open('Second_kurs', 'r')
    groups2 = file.read().splitlines()
    for i, groups2 in enumerate(groups2):
        print(i+1, groups2)
    mes1 = int(input("Enter your group: "))
    file.close()
    with open('Second_kurs') as f:
        lines = f.readlines()
        print(lines[mes1-1])
    f = open('New_Group1', 'r+')
    f.write("Groups name: ")
    f.write(lines[mes1-1])
    f.close()
    create_people2()


def third_kurs(kurs):
    print(f"You have chosen the {kurs} course")
    group_quantity = int(
        input(f"How many groups are there in the {kurs} year? "))
    generate_random_groups_bacalavr_third(group_quantity)
    print("Find your group in this list: ")
    groups3 = []
    file = open('Third_kurs', 'r')
    groups3 = file.read().splitlines()
    for i, groups3 in enumerate(groups3):
        print(i+1, groups3)
    mes1 = int(input("Enter your group: "))
    file.close()
    with open('Third_kurs') as f:
        lines = f.readlines()
        print(lines[mes1-1])
    f = open('New_Group2', 'r+')
    f.write("Groups name: ")
    f.write(lines[mes1-1])
    f.close()
    create_people3()


def fourth_kurs(kurs):
    print(f"You have chosen the {kurs} course")
    group_quantity = int(
        input(f"How many groups are there in the {kurs} year? "))
    generate_random_groups_bacalavr_fourth(group_quantity)
    print("Find your group in this list: ")
    groups4 = []
    file = open('Fourth_kurs', 'r')
    groups4 = file.read().splitlines()
    for i, groups4 in enumerate(groups4):
        print(i+1, groups4)
    mes1 = int(input("Enter your group: "))
    file.close()
    with open('Fourth_kurs') as f:
        lines = f.readlines()
        print(lines[mes1-1])
    f = open('New_Group3', 'r+')
    f.write("Groups name: ")
    f.write(lines[mes1-1])
    f.close()
    create_people4()


def bacalavr_level(kurs_number):
    if kurs_number == 'q':
        pass
    elif kurs_number == 1:
        first_kurs(kurs_number)
    elif kurs_number == 2:
        second_kurs(kurs_number)
    elif kurs_number == 3:
        third_kurs(kurs_number)
    elif kurs_number == 4:
        fourth_kurs(kurs_number)
    else:
        print("Go away from my shit code!")


def generate_random_groups_bacalavr_first(a):
    f = open('First_kurs', 'w')
    for i in range(a):
        letters = string.ascii_lowercase
        rand_letters = ''.join(random.choice(letters) for i in range(2))
        number = randrange(10, 20, 2)
        f.write(f"{rand_letters}-{number}\n")
    f.close()


def generate_random_groups_bacalavr_second(a):
    f = open('Second_kurs', 'w')
    for i in range(a):
        letters = string.ascii_lowercase
        rand_letters = ''.join(random.choice(letters) for i in range(2))
        number = randrange(20, 30, 2)
        f.write(f"{rand_letters}-{number}\n")
    f.close()


def generate_random_groups_bacalavr_third(a):
    f = open('Third_kurs', 'w')
    for i in range(a):
        letters = string.ascii_lowercase
        rand_letters = ''.join(random.choice(letters) for i in range(2))
        number = randrange(30, 40, 2)
        f.write(f"{rand_letters}-{number}\n")
    f.close()


def generate_random_groups_bacalavr_fourth(a):
    f = open('Fourth_kurs', 'w')
    for i in range(a):
        letters = string.ascii_lowercase
        rand_letters = ''.join(random.choice(letters) for i in range(2))
        number = randrange(40, 50, 2)
        f.write(f"{rand_letters}-{number}\n")
    f.close()


def create_people():
    f = open("New_Group", 'a')
    cout = 0
    for i in range(randint(15, 25)):
        f.write(names.get_full_name())
        f.write("\n")
        cout += 1
    f.write(f"This group of {cout} people.")


def create_people2():
    f = open("New_Group1", 'a')
    cout = 0
    for i in range(randint(15, 25)):
        f.write(names.get_full_name())
        f.write("\n")
        cout += 1
    f.write(f"This group of {cout} people.")


def create_people3():
    f = open("New_Group2", 'a')
    cout = 0
    for i in range(randint(15, 25)):
        f.write(names.get_full_name())
        f.write("\n")
        cout += 1
    f.write(f"This group of {cout} people.")


def create_people4():
    f = open("New_Group3", 'a')
    cout = 0
    for i in range(randint(15, 25)):
        f.write(names.get_full_name())
        f.write("\n")
        cout += 1
    f.write(f"This group of {cout} people.")





if __name__ == "__main__":
    direction()
