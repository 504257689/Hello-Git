import json

class Student:
    def __init__(self, name, age, gender, student_id, hobbies, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.hobbies = hobbies
        self.gpa = gpa

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'student_id': self.student_id,
            'hobbies': self.hobbies,
            'gpa': self.gpa
        }

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, 'r') as file:
                students = json.load(file)
                return [Student(**student) for student in students]
        except FileNotFoundError:
            return []

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, name, age, gender, student_id, hobbies, gpa):
        new_student = Student(name, age, gender, student_id, hobbies, gpa)
        self.students.append(new_student)
        self.save_students()

    def delete_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        self.save_students()

    def sort_students(self, key):
        self.students.sort(key=lambda student: getattr(student, key))
        self.save_students()

    def view_students(self):
        return [student.to_dict() for student in self.students]

    def menu(self):
        while True:
            print("\n学生信息管理系统")
            print("1. 添加学生")
            print("2. 查看学生")
            print("3. 排序学生")
            print("4. 删除学生")
            print("5. 退出")
            choice = input("请选择操作: ")

            if choice == '1':
                self.add_student_interactive()
            elif choice == '2':
                self.view_students_interactive()
            elif choice == '3':
                self.sort_students_interactive()
            elif choice == '4':
                self.delete_student_interactive()
            elif choice == '5':
                break
            else:
                print("无效选择，请重试。")

    def add_student_interactive(self):
        name = input("请输入学生名字: ")
        age = int(input("请输入学生年龄: "))
        gender = input("请输入学生性别: ")
        student_id = input("请输入学生学号: ")
        hobbies = input("请输入学生爱好（用逗号分隔）: ").split(',')
        gpa = float(input("请输入学生绩点: "))
        self.add_student(name, age, gender, student_id, hobbies, gpa)
        print("学生已添加。")

    def view_students_interactive(self):
        students = self.view_students()
        if students:
            for i, student in enumerate(students, start=1):
                print(f"\n学生 {i}:")
                print(f"名字: {student['name']}")
                print(f"年龄: {student['age']}")
                print(f"性别: {student['gender']}")
                print(f"学号: {student['student_id']}")
                print(f"爱好: {', '.join(student['hobbies'])}")
                print(f"绩点: {student['gpa']}")
        else:
            print("当前没有学生信息。")

    def sort_students_interactive(self):
        key = input("请按属性排序（名字、年龄、性别、学号、绩点）: ")
        if key in ['name', 'age', 'gender', 'student_id', 'gpa']:
            self.sort_students(key)
            print(f"学生已按 {key} 排序。")
        else:
            print("无效排序属性。")

    def delete_student_interactive(self):
        student_id = input("请输入要删除的学生学号: ")
        self.delete_student(student_id)
        print("学生已删除。")

# 示例用法
if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()