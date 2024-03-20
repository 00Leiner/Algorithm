class availability_domain:
    def __init__(self, teachers, students, rooms, days, timeslots) -> None:
        self.teachers = teachers
        self.students = students
        self.rooms = rooms
        self.days = days
        self.timeslots = timeslots
        
    def teacher_availability_domain(self):
        return {teacher['_id']: {day: {time: [] for time in self.timeslots}for day in self.days}for teacher in self.teachers}

    def student_availability_domain(self):
        return{student['_id']: {day: {time: [] for time in self.timeslots}for day in self.days}for student in self.students}

    def room_availability_domain(self):
        return{room['_id']: {day: {time: [] for time in self.timeslots}for day in self.days}for room in self.rooms}
