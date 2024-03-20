from faker import Faker
import random
from datetime import datetime, timedelta
import configparser
import pandas as pd
from dateutil.relativedelta import relativedelta
import xlsxwriter

config = configparser.ConfigParser()
fake = Faker('pl_PL')

mode = 't1'
global_id = 0

profiles = {}
students = {}
grades = {}
classes = {}
attendances = {}
teachers = {}
results = {}

used_names = set()

def get_global_id():
    global global_id
    global_id += 1
    return global_id


def save_students():
    if mode == 't1':
        with open("students.bulk", 'w') as file:
            for student_id, student in students.items():

                endIter = len(student.values())
                i = 1

                for key, value in student.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")
    elif mode == 't2':
        with open("students_t2.bulk", 'w') as file:
            for student_id, student in students.items():

                endIter = len(student.values())
                i = 1

                for key, value in student.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")

def save_teachers():
    if mode == 't1':
        with open("teachers_t1.bulk", 'w') as file:
            for teacher_id, teacher in teachers.items():

                endIter = len(teacher.values())
                i = 1

                for key, value in teacher.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")
    else:
        with open("teachers_t2.bulk", 'w') as file:
            for teacher_id, teacher in teachers.items():

                endIter = len(teacher.values())
                i = 1

                for key, value in teacher.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")

def save_grades():
    if mode == 't1':
        with open("grades_t1.bulk", 'w') as file:
            for grade_id, grade in grades.items():

                endIter = len(grade.values())
                i = 1

                for key, value in grade.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")
    else:
        with open("grades_t2.bulk", 'w') as file:
            for grade_id, grade in grades.items():

                endIter = len(grade.values())
                i = 1

                for key, value in grade.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")

#dorobic skippowanie current_number_of
def save_classes():
    if mode == 't1':
        with open("classes_t1.bulk", 'w') as file:
            for class_id, _class in classes.items():

                endIter = len(_class.values())
                i = 1

                for key, value in _class.items():

                    if(key != "curr_num_of_students"):
                        if i != endIter:
                            file.write(str(value) + "|")
                        else:
                            file.write(str(value))

                    i += 1

                file.write("\n")
    else:
        with open("classes_t2.bulk", 'w') as file:
            for class_id, _class in classes.items():

                endIter = len(_class.values())
                i = 1

                for key, value in _class.items():

                    if (key != "curr_num_of_students"):
                        if i != endIter:
                            file.write(str(value) + "|")
                        else:
                            file.write(str(value))

                    i += 1

                file.write("\n")

def save_attendance():
    if mode == 't1':
        with open("attendances_t1.bulk", 'w') as file:
            for att_id, att in attendances.items():

                endIter = len(att.values())
                i = 1

                for key, value in att.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")
    else:
        with open("attendances_t2.bulk", 'w') as file:
            for att_id, att in attendances.items():

                endIter = len(att.values())
                i = 1

                for key, value in att.items():
                    if i != endIter:
                        file.write(str(value) + "|")
                    else:
                        file.write(str(value))

                    i += 1

                file.write("\n")

def save_profiles():
    with open("profiles.bulk", 'w') as file:
        for prof_id, prof in profiles.items():

            endIter = len(prof.values())
            i = 1

            for key, value in prof.items():
                if i != endIter:
                    file.write(str(value) + "|")
                else:
                    file.write(str(value))

                i += 1

            file.write("\n")

def generate_profiles():

    profile_names = ["Mathematics and Physics", "Informatics", "Chemistry and Biology", "Linguistics",
                        "History and Social Sciences", "Art and Architecture"]
    descriptions = [
        "The \"Mathematics and Physics\" class profile delves into the fundamental principles and interconnections between mathematics and physics, exploring the intricate relationship between these disciplines. Students engage in problem-solving, theoretical exploration, and practical applications, unlocking the underlying laws governing the universe and shaping our understanding of natural phenomena through the lens of mathematical reasoning and physical laws.",
        "The \"Informatics\" class profile focuses on the study of computational systems, information processing, and the utilization of technology to solve real-world problems. Students delve into various aspects of computer science, data analysis, information theory, and technological applications, honing skills in programming, problem-solving, and understanding the impact of information technology on society and innovation. This course equips learners with the knowledge and tools to navigate the digital landscape and harness the power of information for diverse fields and industries.",
        "The \"Chemistry and Biology\" class profile immerses students in the exploration of life sciences through the lens of chemical processes and biological systems. This interdisciplinary course delves into the intricacies of molecular interactions, cellular structures, and the chemical foundations of life. Students analyze the relationship between chemistry and biology, examining topics such as biochemistry, molecular biology, and the application of scientific principles to understand living organisms and their environments. Through experiments, analysis, and theoretical study, learners gain insights into the complexities of life at a molecular level.",
        "The \"Linguistics\" class profile delves into the scientific study of language, encompassing its structure, evolution, and diverse usage. Students explore the intricacies of human communication, analyzing phonetics, syntax, semantics, and language acquisition. This course examines the cultural, social, and cognitive aspects of language, offering insights into multilingualism, language preservation, and the role of language in society. Through research, analysis, and theoretical exploration, students gain a deeper understanding of the complexities and significance of human language and its impact on various aspects of our lives.",
        "The \"History and Social Sciences\" class profile immerses students in the exploration of humanity's past and the complexities of societal structures. Students delve into historical events, societal norms, cultural dynamics, and human behavior across different eras and civilizations. This interdisciplinary course integrates the study of history with social sciences, encompassing sociology, anthropology, political science, and economics. Students analyze the connections between historical events and their impact on contemporary society, fostering critical thinking, cultural awareness, and a deeper understanding of the forces shaping human societies.",
        "The \"Art and Architecture\" class profile is an immersive exploration of creative expression and structural design. Students delve into the realms of artistic creation, architectural principles, and the interconnectedness between art and built environments. The course encompasses various art forms, design elements, and historical movements, examining how art and architecture reflect cultural influences and human creativity. Students analyze aesthetics, spatial design, and the evolution of architectural styles, fostering a deep understanding of how art and architecture shape our environment and contribute to the cultural tapestry of human civilization."
    ]

    for i in range(len(profile_names)):
            
        profile_id = get_global_id()

        profiles[profile_id] = {"profile_id" : profile_id, "profile_name" : profile_names[i], "descriptions" : descriptions[i]}



def generate_students(num_of_entries):

    for _ in range(num_of_entries):
        student_id = get_global_id()
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth(minimum_age=15, maximum_age=20)
        gender = "M"
        if first_name[-1] == "a" or first_name[-1] == "e":
            gender = "F"
        address = fake.address()
        phone_number = fake.phone_number()
        email = first_name.lower() + last_name.lower() + "@email.com"
        admission_date = date_of_birth.replace(year=date_of_birth.year + 15, month=8, day=15)
        graduation_date = admission_date.replace(year=admission_date.year + 3, month=5, day=31)
        #profile_id =
        #class_id =

        students[student_id] = {"student_id" : student_id, "first_name" : first_name, "last_name" : last_name, "date_of_birth" : date_of_birth, 
                            "gender" : gender, "address" : address, "phone_number" : phone_number, "email" : email, "admission_date" : admission_date,
                            "graduation_date" : graduation_date, "profile_id" : 0, "class_id" : 0}


def generate_grades(num_of_entries):

    for _ in range(num_of_entries):
        grade_id = get_global_id()
        subject = fake.random_element(elements=('Mathematics', 'English', 'Physics', 'History', 'Art', 'Computer Science', 'Music', 'Geography', 'Physical education', 'Polish language'))
        percentage = fake.random_int(min=0, max=100)
        grade = fake.random_int(min=1, max=6)
        comments = fake.random_element(elements=('Bad', 'Really Bad', 'Good', 'Really Good', 'Average'))

        date_of_birth = fake.date_of_birth(minimum_age=15, maximum_age=20)

        admission_date = date_of_birth.replace(year=date_of_birth.year + 15, month=8, day=15)
        graduation_date = admission_date.replace(year=admission_date.year + 3, month=5, day=31)

        assign_date = fake.date_between_dates(date_start=admission_date, date_end=graduation_date)
        time = fake.time()

        grades[grade_id] = {"grade_id" : grade_id, "subject" : subject, "percentage" : percentage, "grade" : grade, "comments" : comments, "student_id" : 0, "teacher_id" : 0,
                            "assign_date" : assign_date, "assign_time": time}

def generate_classes(num_of_entries):

    for i in range(num_of_entries):
        class_id = get_global_id()
        class_name = str(fake.random_int(min=1, max=3)) + fake.random_element(elements=('A','B','C','D','E','F'))
        while class_name in used_names:
            class_name = str(fake.random_int(min=1, max=3)) + fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F'))
        number_of_students = fake.random_int(min=20, max=20)
        curr_num_of_students = 0
               
        #file.write("{0}|{1}|{2}|{3}".format(class_id, class_name, number_of_students, isOnline))
        classes[class_id] = {"class_id" : class_id, "class_name" : class_name, "number_of_students": number_of_students, "curr_num_of_students" : curr_num_of_students,
                        "profile_id" : 0}
        used_names.add(class_name)

def generate_attendance(num_of_entries):

    if mode == 't2':
        for attendance_id, attendance in attendances.items():
            if not attendance['present']:
                prob = random.random()
                if prob >= 0.75:
                    attendance['present'] = True


    for _ in range(num_of_entries):
        attendance_id = get_global_id()
        #date
        room_number = str(fake.random_int(1, 400))
        #teacher_id
        number_of_hours = fake.random_int(1, 3)
        present = fake.random_element(elements=(True, False))
        subject = fake.random_element(elements=('Mathematics', 'English', 'Physics', 'History', 'Art', 'Computer Science', 'Music', 'Geography', 'Physical education', 'Polish language'))
        isExtracullicular = fake.random_element(elements=(True, False))
        isOnline = fake.random_element(elements=(True, False))

        date_of_birth = fake.date_of_birth(minimum_age=15, maximum_age=20)

        admission_date = date_of_birth.replace(year=date_of_birth.year + 15, month=8, day=15)
        graduation_date = admission_date.replace(year=admission_date.year + 3, month=5, day=31)

        date = fake.date_between_dates(date_start=admission_date, date_end=graduation_date)
        time = fake.time()
        attendances[attendance_id] = {"attendance_id" : attendance_id, "room_number" : room_number, "number_of_hours" : number_of_hours, "present" : present, 
                            "isExtracullicular" : isExtracullicular, "isOnline" : isOnline, "subject" : subject, "student_id" : 0, "teacher_id" : 0, "date" : date, "time": time}

def generate_teachers(num_of_entries):

    for _ in range(num_of_entries):
        teacher_id = get_global_id()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = first_name.lower() + last_name.lower() + "@email.com"
        phone_number = fake.phone_number()
        hire_date = fake.date_between()
        specialization = fake.random_element(elements=('Mathematics', 'English', 'Physics', 'History', 'Art', 'Computer Science', 'Music', 'Geography', 'Physical education', 'Polish language'))
        experience_years = datetime.today().year - hire_date.year
        age = datetime.today().year - fake.date_of_birth(minimum_age=25, maximum_age=60).year

        #file.write("{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}".format(teacher_id, first_name, last_name, email, phone_number, hire_date, specialization, experience_years, age))
        teachers[teacher_id] = {"teacher_id" : teacher_id, "first_name" : first_name, "last_name" : last_name, "email" : email, "phone_number" : phone_number, "hire_date" : hire_date, 
                            "specialization" : specialization, "experience_years" : experience_years, "age" : age}


def generate_results():
    global mode
    if mode == 't1':
        for student_id, student in students.items():
            _id = student_id
            first_name = student['first_name']
            last_name = student['last_name']
            grad_date = str(student['graduation_date']).split('-')
            if datetime(int(grad_date[0]), int(grad_date[1]), int(grad_date[2])) <= datetime.today()-relativedelta(years=1):
                dates_rand = []
                for _ in range(1):
                    rand_date = fake.date_between(student['graduation_date'] - relativedelta(months=1), student['graduation_date'])
                    dates_rand.append(rand_date)
                dates = "{0}".format(dates_rand[0])
                subjects_rand = random.sample(['Mathematics', 'English', 'Physics', 'History', 'Art', 'Computer Science', 'Music', 'Geography', 'Physical education', 'Polish language'], k=1)
                subjects = "{0}".format(subjects_rand[0])
                results_rand = []
                for _ in range(1):
                    results_rand.append(random.randint(20, 100))
                res = "{0}%".format(str(results_rand[0]))
                results[_id] = {"student_id" : _id, "first_name" : first_name, "last_name" : last_name, "subjects" : subjects, "dates_of_exams" : dates, "results" : res}
            else:
                results[_id] = {"student_id" : _id, "first_name" : first_name, "last_name" : last_name, "subjects" : "", "dates_of_exams" : "", "results" : ""}
    else:
        for result_id, result in results.items():
            if result['subjects'] == "":
                grad_date = str(students[result['student_id']]['graduation_date']).split('-')
                if datetime(int(grad_date[0]), int(grad_date[1]), int(grad_date[2])) < datetime.today():
                    dates_rand = []
                    for _ in range(1):
                        rand_date = fake.date_between(students[result['student_id']]['graduation_date'] - relativedelta(months=1),
                                                      students[result['student_id']]['graduation_date'])
                        dates_rand.append(rand_date)
                    dates = "{0}".format(dates_rand[0])
                    subjects_rand = random.sample(
                        ['Mathematics', 'English', 'Physics', 'History', 'Art', 'Computer Science', 'Music',
                         'Geography', 'Physical education', 'Polish language'], k=1)
                    subjects = "{0}".format(subjects_rand[0])
                    results_rand = []
                    for _ in range(1):
                        results_rand.append(random.randint(20, 100))
                    res = "{0}%".format(str(results_rand[0]))
                    result['subjects'] = subjects
                    result['dates_of_exams'] = dates
                    result['results'] = res



def make_relationships_student_profile_class():

    global classes
    global students

    min_class_index = 0

    for student_id, student in students.items():

        for class_id, _class in classes.items():
          
            if(_class["curr_num_of_students"] < _class["number_of_students"]):
                _class["curr_num_of_students"] += 1
                student["class_id"] = _class["class_id"]
                break

    for class_id, _class in classes.items():

        _class["profile_id"] = random.choice(list(profiles.keys()))

    for student_id, student in students.items():

        student["profile_id"] = classes[student["class_id"]]["profile_id"]

                

def make_relationships_student_grade_teacher_attendance():

    global students
    global attendances
    global teachers
    global grades

    teachers_by_specialization = {}
    students_by_class_id = {}

    class_date_counts = {}

    max_in_one_day = 10

    for teacher_id, teacher in teachers.items():

        if teacher["specialization"] in teachers_by_specialization:
            teachers_by_specialization[teacher["specialization"]].append(teacher_id)
        else:
            teachers_by_specialization[teacher["specialization"]] = [teacher_id]

    for student_id, student in students.items():

        if student["class_id"] in students_by_class_id:
            students_by_class_id[student["class_id"]].append(student_id)
        else:
            students_by_class_id[student["class_id"]] = [student_id]
    

    new_attendances = {}


    for attendance_id, attendance in attendances.items():

        attendance["teacher_id"] = random.choice(teachers_by_specialization[attendance["subject"]])
        
        random_class_id = random.choice(list(classes.keys()))

        if (str(random_class_id) + str(attendance["date"])) in class_date_counts:

            if class_date_counts[str(random_class_id) + str(attendance["date"])] >= max_in_one_day: #if failed to found it will assign for more than the limit
                for class_id in classes.keys():
                    if class_date_counts[str(class_id) + str(attendance["date"])] < max_in_one_day:
                        random_class_id = class_id
                        break

            class_date_counts[str(random_class_id) + str(attendance["date"])] += 1

        else: class_date_counts[str(random_class_id) + str(attendance["date"])] = 0

        first_iteration = True

        for student_id in students_by_class_id[random_class_id]:

            if first_iteration:
                attendance["student_id"] = student_id
                first_iteration = False
                #{"attendance_id" : attendance_id, "room_number" : room_number, "number_of_hours" : number_of_hours, "present" : present, 
                            #"isExtracullicular" : isExtracullicular, "isOnline" : isOnline, "subject" : subject, "student_id" : 0, "teacher_id" : 0, "date" : date}
            else:
                new_attendance_id = get_global_id()
                new_attendances[new_attendance_id] = {"attendance_id" : new_attendance_id, "room_number" : attendance["room_number"], 
                                                    "number_of_hours" : attendance["number_of_hours"], "present" : attendance["present"], 
                                                    "isExtracullicular" : attendance["isExtracullicular"], "isOnline" : attendance["isOnline"], 
                                                    "subject" : attendance["subject"],
                                                    "student_id" : student_id, "teacher_id" : attendance["teacher_id"],
                                                    "date" : attendance["date"], "time": fake.time()}

    #copy new attendances into attendances
    for new_attendance_id, new_attendance in new_attendances.items():

        attendances[new_attendance_id] = {"attendance_id" : new_attendance_id, "room_number" : new_attendance["room_number"], 
                                        "number_of_hours" : new_attendance["number_of_hours"], "present" : new_attendance["present"], 
                                        "isExtracullicular" : new_attendance["isExtracullicular"], "isOnline" : new_attendance["isOnline"], 
                                        "subject" : new_attendance["subject"],
                                        "student_id" : new_attendance["student_id"], "teacher_id" : new_attendance["teacher_id"],
                                        "date" : new_attendance["date"], "time": new_attendance["time"]}

    for attendance_id, attendance in attendances.items():

        if fake.random_int(1, 10) == 2:

            grade_id = get_global_id()

            grades[grade_id] = {"grade_id" : grade_id, "subject" : attendance["subject"], "percentage": fake.random_int(min=0, max=100), "grade" : fake.random_int(1, 6), "comments": fake.random_element(elements=('Bad', 'Really Bad', 'Good', 'Really Good', 'Average')),"student_id" : attendance["student_id"],
                                "teacher_id" : attendance["teacher_id"], "assign_date" : attendance["date"], "assign_time":attendance["time"]}


# T1 - start of the academic year
config.read('config.ini')

# generation of T1 data for the database
generate_students(int(config['T1']['num_of_students'])) #studentow ma byc 20 razy tyle co classes, kazda klasa ma miec rowno 20 studentow, bo jak nie to nie wyjdzie no...
generate_profiles()
generate_classes(int(config['T1']['num_of_classes']))
generate_attendance(int(config['T1']['num_of_attendances']))

generate_teachers(int(config['T1']['num_of_teachers']))
generate_grades(int(config['T1']['num_of_grades']))

make_relationships_student_profile_class()
make_relationships_student_grade_teacher_attendance()

save_students()
save_classes()
save_profiles()
save_attendance()
save_teachers()
save_grades()

generate_results()


# load teachers to excel

# Excel sheets and Exam results_T1

writer = pd.ExcelWriter('PrincipalsExcel.xlsx', engine='xlsxwriter')
df11 = pd.DataFrame(results.values(), index=results.keys())
df11.to_excel(writer, sheet_name='Exam_results_T1')



# T2 - end of the academic year

mode = 't2'

generate_attendance(int(config['T2']['num_of_attendances']))
generate_grades(int(config['T2']['num_of_grades']))
make_relationships_student_profile_class()
make_relationships_student_grade_teacher_attendance()

#cos tam z baza danych
#dac wiecej ocen, zwiekszyc nauczycielom experience o rok i age też o rok
#zmienic losowe kilka nieobecnosci na obecnosci, dodac wiecej attendances

# Excel sheet Teachers_T2 and Exam results_T2
for teacher_id, teacher in teachers.items():
    teacher['age'] += 1
    teacher['experience_years'] += 1

generate_teachers(int(config['T2']['num_of_teachers']))
save_teachers()
save_attendance()
save_grades()

generate_results()

df2 = pd.DataFrame(teachers.values(), index=teachers.keys())
df22 = pd.DataFrame(results.values(), index=results.keys())
df2.to_excel(writer, sheet_name='Teachers_T2')
df22.to_excel(writer, sheet_name='Exam Results_T2')
writer.close()
