from utils.remote import remotes

class assignment_domain:
    def __init__(self):
        self._remotes = remotes()

    def assignment(self):
        domain_schedule = {}
        
        _student_dictionary = self._remotes.student_dictionary()
        for student in _student_dictionary:
            _type = student['course_type']
            _code = student['course_code']
            _id = student['student_id']
            domain_schedule[_id] = {
                'course': _code,
                'teacher': None,
                'room': None,
                'day': None,
                'time': None
            }
            _teacher_dictionary = self._remotes.teacher_dictionary(_code)
            _room_dictionary = self._remotes.room_dictionary(_type)
            _day_dictionary = self._remotes.day_dictionary()
            _timeslot_dictionary = self._remotes.timeslot_dictionary(_type)
            
            domain_schedule[(_id)]['teacher'] = {teachers for teachers in _teacher_dictionary}
            domain_schedule[(_id)]['room']= {(room1, room2) for (room1, room2) in _room_dictionary}
            domain_schedule[(_id)]['day'] = {(da1, day2) for (da1, day2) in _day_dictionary}
            domain_schedule[(_id)]['time'] = {(time1, time2) for (time1, time2) in _timeslot_dictionary}

        return domain_schedule