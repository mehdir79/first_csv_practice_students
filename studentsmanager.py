import csv

def add_new_student():
    new_student = dict(name , family_name,class_num,math , science , literature)
    try:
        new_student["name"] = input("enter the students name:\n")
        new_student["family_name"] = input("enter students family name:\n")
        new_student["class_num"] = int(input("enter students class number:\n"))
        new_student["math"] = float(input("enter students math score:\n"))
        new_student["science"] =float(input("enter students sciense score:\n"))
        new_student["literature"] = float(input("enter students literature score:\n"))
    except:
        print("wring input!")
        return
    with open("students.csv",'w+') as stcsv:
        stcsvreader = csv.reader(stcsv)
        stcsvwrighter = csv.writer(stcsv)
        if stcsvreader.line_num()==0:
            stcsvwrighter.writerow("name" , "family_name","class_num","math", "science" , "literature")
        
def show_all_students_in_table():
    return

def show_students_avg_by_familyname():
    return

def who_is_the_best_student():
    return

def search_by_familyname_or_class_num():
    return

def exit_program():
    exit()

while True:
    action = int(input("what do you whant to do?\n1: add new student\n2: show all students\n3: show student avg by familyname\n4: show best student\n5: search by family name or class num\n6: exit\n"))
    match action:
        case 1:
            add_new_student()
        case 2:
            show_all_students_in_table()
        case 3:
            show_students_avg_by_familyname()
        case 4:
            who_is_the_best_student()
        case 5:
            search_by_familyname_or_class_num()
        case 6:
            exit_program()
        case _:
            print("wrong input! try again:")