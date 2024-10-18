from tabulate import tabulate

class University:
    def __init__(self):
        self.students = []  # List to store student objects
        self.teachers = []  # List to store teacher objects
        self.sections = []  # List to store section objects

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_section(self, section):
        self.sections.append(section)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Human):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


class Section:
    def __init__(self, section_name, teacher, students, class_time):
        self.section_name = section_name
        self.teacher = teacher  # Teacher object
        self.students = students  # List of Student objects
        self.class_time = class_time  # Time required for the class

    def get_info(self):
        return {
            "section_name": self.section_name,
            "teacher": self.teacher.name,
            "number_of_students": len(self.students),
            "class_time": self.class_time
        }


# Example Usage
university = University()

# Adding students
student1 = Student("Ali", 20, "S001")
student2 = Student("Mursalen", 21, "S002")
university.add_student(student1)
university.add_student(student2)

# Adding teachers
teacher1 = Teacher("Mr. Sheran", 40, "T001")
university.add_teacher(teacher1)

# Adding sections
section1 = Section("Batch 65", teacher1, [student1, student2], "02:00 PM - 06:00 PM")
university.add_section(section1)

# Prepare data for table display
table_data = []
for section in university.sections:
    info = section.get_info()
    table_data.append([
        info['section_name'],
        info['teacher'],
        info['number_of_students'],
        info['class_time']
    ])

# Display section information in table format
print(tabulate(table_data, headers=["Section Name", "Teacher", "Number of Students", "Class Time"], tablefmt="grid"))
