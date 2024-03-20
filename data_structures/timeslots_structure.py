class timeslot:
    def __init__(self, hours) -> None:
        self.hours = hours
        self.three_hours = set()
        self.two_hours = set()
        self.one_hour = set()
        self.generate_timeslots()

    def generate_timeslots(self):
        list_of_timeslots = list(self.hours)
        for i in range(len(list_of_timeslots) - 2):
            self.three_hours.add((list_of_timeslots[i], list_of_timeslots[i + 2]))
        for i in range(len(list_of_timeslots) - 1):
            self.two_hours.add((list_of_timeslots[i], list_of_timeslots[i + 1]))
        for i in range(len(list_of_timeslots) - 1):
            self.one_hour.add((list_of_timeslots[i], list_of_timeslots[i + 1]))

    def timeslot_dictionary(self, course_type):
        c_type = course_type.lower()
        if c_type == "laboratory":
            return {(time1, time2) for time1 in self.three_hours for time2 in self.two_hours}
        if c_type == "lecture":
            return {(time1, time2) for time1 in self.two_hours for time2 in self.one_hour}
        print(f"error in slots_dictionary: {c_type}")
