ids = []
names = []
dobs = []

def student(sid, sname, sdob):
    ids.append(sid)
    names.append(sname)
    dobs.append(sdob)

n = int(input("Enter the number of students: "))

for i in range(1, n + 1):
    print("\nStudent " + str(i) + ":")
    student_id = str(input("\tEnter the student's ID: "))
    full_name = str(input("\tEnter the student's full name: "))
    birth_date = str(input("\tEnter the student's date of birth: "))
    student(student_id, full_name, birth_date)

print("\nList of students:")
for s in range(0, n):
    print(str(s + 1) + ")" + "\t\tStudent ID: " + ids[s] + "\t\tFull name: " + names[s] + "\t\tDate of birth: " + dobs[s])

print("\n")

idc = []
namec = []

def course(cid, cname):
    idc.append(cid)
    namec.append(cname)

m = int(input("Enter the number of courses: "))

for j in range(1, m + 1):
    print("\nCourse " + str(j) + ":")
    course_id = str(input("\tEnter the course ID: "))
    course_name = str(input("\tEnter the course name: "))
    course(course_id, course_name)

print("\nList of courses:")
for c in range(0, m):
    print(str(c + 1) + ")" + "\t\tCourse ID: " + idc[c] + "\t\tCourse name: " + namec[c])

marks = []

def marksheet(grades):
    print("Mark sheet:")
    for g in range(0, len(grades)):
        print(str(g + 1) + ")" + "\t\t", grades[g])

print("\n")

print("Mark input:")

for st in range(1, len(ids) + 1):
    new_mark = {}
    studid = str(input("\nEnter the " + str(st) + "th" + " student's ID: "))
    sindex = ids.index(studid)
    new_mark["Student ID"] = ids[sindex]
    new_mark["Full name"] = names[sindex]
    new_mark["Date of birth"] = dobs[sindex]
    for cor in range(1, len(idc) + 1):
        corid = str(input("\tEnter the " + str(cor) + "th" + " course ID: "))
        cindex = idc.index(corid)
        mark = float(input("\t\tEnter the " + str(cor) + "th" + " course mark: "))
        new_mark[namec[cindex]] = mark
    marks.append(new_mark)

print("\n")

marksheet(marks)
