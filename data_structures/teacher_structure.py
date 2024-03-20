class teacher:
    def __init__(self, teachers) -> None:
        self.teachers = teachers
        self.teacher_structure = []
        self._teacher()

    def _teacher(self):
        for teacher in self.teachers:
            for specialized in teacher['specialized']:
                self.teacher_structure.append({
                    "teacher_id": teacher['_id'],
                    "specialized_code": specialized['code'],
                })

    def teacher_dictionary(self, course_code):
        return {teacher['teacher_id'] for teacher in self.teacher_structure if teacher['specialized_code'] == course_code}