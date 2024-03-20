from fetch_data.course_data import fetch_course_data
from fetch_data.room_data import fetch_room_data
from fetch_data.student_data import fetch_student_data
from fetch_data.teacher_data import fetch_teacher_data
from data_structures.days_structure import _days
from data_structures.room_structure import room
from data_structures.student_structure import student
from data_structures.teacher_structure import teacher
from data_structures.timeslots_structure import timeslot
from domain.availability_domain import availability_domain
from utils.data_format import data_format

class remotes:
    def __init__(self) -> None:
        self.courses = fetch_course_data()
        self.rooms = fetch_room_data()
        self.students = fetch_student_data()
        self.teachers = fetch_teacher_data()
        self.days = range(1,7) #monday - saturday
        self.hours = range(7,20) #7am-7pm 
        self.availability = availability_domain(self.teachers, self.students, self.rooms, self.days, self.hours)
        self.num_solution = 2 #number of solution
    
    def data_format(self, result):
        student_details = {student['_id']: student for student in self.students}
        course_details = {course['code']: course for course in self.courses}
        teacher_details = {teacher['_id']: teacher for teacher in self.teachers}
        room_details = {room['_id']: room for room in self.rooms}
        _data_format = data_format(teacher_details, student_details, room_details, course_details)
        return _data_format.data_format(result)

    def number_of_solution(self):
        return self.num_solution

    def student_dictionary(self):
        _student = student(self.students)
        return _student.student_dictionary()

    def teacher_dictionary(self, _code):
        _teacher = teacher(self.teachers)
        return _teacher.teacher_dictionary(_code)
    
    def room_dictionary(self, _type):
        _room = room(self.rooms)
        return _room.room_dictionary(_type)
    
    def day_dictionary(self):
        _day = _days(self.days)
        return _day.days_dictionary()

    def timeslot_dictionary(self, _type):
        _time = timeslot(self.hours)
        return _time.timeslot_dictionary(_type)
    
    #availability dictionary
    def teacher_availability_dictionary(self):
        return self.availability.teacher_availability_domain()
    def student_availability_dictionary(self):
        return self.availability.student_availability_domain()
    def room_availability_dictionary(self):
        return self.availability.room_availability_domain()