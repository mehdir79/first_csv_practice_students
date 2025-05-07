import csv , os
import matplotlib

csv_fields = list()
csv_data = list()



def add_new_student():
    new_student = dict(name = "" ,family_name = "" , class_num = 0 , math = 0 , science = 0 , literature = 0)
    try:
        new_student["name"] = input("enter the students name:")
        new_student["family_name"] = input("enter students family name:")
        new_student["class_num"] = int(input("enter students class number:"))
        new_student["math"] = float(input("enter students math score:"))
        new_student["science"] =float(input("enter students science score:"))
        new_student["literature"] = float(input("enter students literature score:"))
    except:
        print("wrong input!")
        return
    with open("students.csv",'a',newline='') as stcsv:
        wrighter  = csv.DictWriter(stcsv ,["name" , "family_name" , "class_num" , "math" , "science" , "literature"] )
        if os.path.getsize("students.csv") == 0:
            wrighter.writeheader()
        wrighter.writerow(new_student)

def show_list():
    csv_fields.clear()
    csv_data.clear()
    with open("students.csv","r") as csv_file:
        stcsv = csv.DictReader(csv_file)
        if(os.path.getsize("students.csv") != 0):
            csv_fields.extend(stcsv.fieldnames)
            for line in stcsv:
                csv_data.append(line)
def show_all_students_in_table():
    with open("students.csv", "r") as students:
        streader = csv.DictReader(students)
        for student in streader:
            print(student)

def show_students_avg_by_familyname():
    with open("students.csv", "r") as students:
        streader = csv.DictReader(students)
        for student in streader: 
            print(f"student {student['name']} {student['family_name']} got avg of = {(float(student['math']) + float(student['science']) + float(student['literature']))/3}")    

def who_is_the_best_student():
    with open("students.csv" , "r") as students:
        best_student = ["" , "" , 0]
        streader = csv.DictReader(students)
        for student in streader:
            if (((float(student['math'])) + float(student['science']) + float(student['literature']))/3) > best_student[2]:
                best_student[0] = student['name']
                best_student[1] = student['family_name']
                best_student[2] = (float(student['math']) + float(student['science']) + float(student['literature']))/3.0
        print(f"best student is : {best_student[0]} {best_student[1]} and got avg of: {best_student[2]}")


def search_by_familyname_or_class_num():
    search_action = input("1: search by family name\n2: search by class-num\n")
    match search_action:
        case "1":
            family = input("enter the familyname: ")
            with open("students.csv" , "r") as students:
                streader = csv.DictReader(students)
                existance = False
                for student in streader:
                    if student['family_name'] == family:
                        existance = True
                        print(student)
                if existance == False:
                    print("student not found!")
                
        case "2":
            class_numin = input("enter the class_num: ")
            with open("students.csv" , "r") as students:
                streader = csv.DictReader(students)
                existance = False
                for student in streader:
                    if str(student['class_num']) == class_numin:
                        existance = True
                        print(student)
                if existance == False:
                    print("class not found!")
                
            
        case _:
            print("wrong input!")
            return
    
def exit_program():
    exit()

while True:
    show_list()
    print(csv_fields)
    action = int(input("what do you want to do?\n1: add new student\n2: show all students\n3: show student avg by familyname\n4: show best student\n5: search by familyname or class num\n6: exit\n"))
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