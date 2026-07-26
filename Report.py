def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 35)
        print("        STUDENT REPORT")
        print("=" * 35)
        func(*args, **kwargs)
        print("=" * 35)
    return wrapper


class Report:

    college = "MIT ADT University"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @classmethod
    def change_template(cls, new_name):
        cls.college = new_name

    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)

        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")



student1 = Report("Rohan Kumar Das", 102, 90)
student1.display_report()

Report.change_template("MIT World Peace University")

student2 = Report("Ashpreet", 100, 39)
student2.display_report()