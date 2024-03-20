from utils.remote import remotes

class schedule_availability_constraints:
    def __init__(self) -> None:
        _remote = remotes()
        self.teacher_availability_dictionary = _remote.teacher_availability_dictionary()
        self.student_availability_dictionary = _remote.student_availability_dictionary()
        self.room_availability_dictionary = _remote.room_availability_dictionary()

    def update_schedule(self, student_id, teacher_id, room_id_1, room_id_2, day1, day2, time1, time2):
        self._update_availability(student_id, teacher_id, room_id_1, day1, time1)
        self._update_availability(student_id, teacher_id, room_id_2, day2, time2)

    def _update_availability(self, student_id, teacher_id, room_id, day, time):
        _time = time
        _day = day
        for t in range(_time[0], _time[1]):
            self.teacher_availability_dictionary[teacher_id][_day][t].append('occupied')
            self.student_availability_dictionary[student_id][_day][t].append('occupied')
            self.room_availability_dictionary[room_id][_day][t].append('occupied')

        rday = _time[1]  # this is for the rest day
        self.student_availability_dictionary[student_id][_day][rday].append('rest')
        self.teacher_availability_dictionary[teacher_id][_day][rday].append('rest')

    def undo_update_schedule(self, student_id, teacher_id, room_id_1, room_id_2, day1, day2, time1, time2):
        self._undo_update_availability(student_id, teacher_id, room_id_1, day1, time1)
        self._undo_update_availability(student_id, teacher_id, room_id_2, day2, time2)

    def _undo_update_availability(self, student_id, teacher_id, room_id, day, time):
        _time = time
        _day = day
        for t in range(_time[0], _time[1]):
            self.teacher_availability_dictionary[teacher_id][_day][t].append('occupied')
            self.student_availability_dictionary[student_id][_day][t].append('occupied')
            self.room_availability_dictionary[room_id][_day][t].append('occupied')

        rday = _time[1]  # this is for the rest day
        self.student_availability_dictionary[student_id][_day][rday].append('rest')
        self.teacher_availability_dictionary[teacher_id][_day][rday].append('rest')