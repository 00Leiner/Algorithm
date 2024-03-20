class student:
    def __init__(self, students) -> None:
        self.students = students

    def student_dictionary(self):
        student_structure = []
        for student in self.students:
            for course in student['courses']:
                student_structure.append({
                    "student_id": student['_id'],
                    "course_code": course['code'],
                    "course_type": course['type'],
                })
        return student_structure
