students=[]
def add_students():
    print('Enter  new student: ')
    name=input('Name:')
    age=input('Age:')
    Grade=input('Grade:')
    try:
        age=int(age)
        Grade=int(Grade)
    except ValueError:
        print('Age and Grade must be intergers. Please try again.')
        return
    #dictory for students
    student={'Name':name, 'Age':age, 'grade':Grade}
    students.append(student)
    print(f'Student{name},has been successfully added')
def student_display():
    if not students:
        print('No student record found')
        return
    for student in students:
        print(f"Name: {student['name']},'Age':{student['age']},{student['Grade']}")
def main():
    while True:
        print('Student Mangement system')
        print('1.Add student name:')
        print('2.Display student records')
        print('3.Exiting program')
        choice=input('Enter your choice(1,2,3)')
        if choice=='1':
            add_students()
        elif choice=='2':
            student_display()
        elif choice=='3':
            print('Exiting the program')
            break
        else:
            print('Invalid choice.Please enter a valid choice')
if __name__=='__main__':
    main()

