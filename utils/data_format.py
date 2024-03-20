class data_format:
        def __init__(self, teachers, students, rooms, courses) -> None:
                self.teachers = teachers
                self.students = students
                self.rooms = rooms
                self.courses = courses
                
        def data_format(self, result):
                formatted_data = []
    
                for options_counter, schedule in enumerate(result, start=1):
                        check_same_student = {}
                        programs = []

                        for student_id, info in schedule.items():
                                course_code = info['course']
                                teacher_id = info['teacher']
                                room1 = info['room'][0]
                                room2 = info['room'][1]
                                day1 = info['day'][0]
                                day2 = info['day'][1]
                                first_day = self.get_day_name(day1)
                                second_day = self.get_day_name(day2)
                                day_sched = f"{first_day}/{second_day}"
                                time1 = info['time'][0]
                                time2 = info['time'][1]
                                first_time = self.get_time(time1)
                                second_time = self.get_time(time2)
                                time_sched = f"{first_time}/{second_time}"

                                if student_id not in check_same_student:
                                        check_same_student[student_id] = {
                                                "program": self.students[student_id]["program"],
                                                "year": self.students[student_id]["year"],
                                                "semester": self.students[student_id]["semester"],
                                                "block": self.students[student_id]["block"],
                                                "sched": []
                                        }
                        
                                student_schedule = {
                                        "courseCode": course_code,
                                        "courseDescription": self.courses[course_code]["description"],
                                        "courseUnit": self.courses[course_code]["units"],
                                        "day": day_sched,
                                        "time": time_sched,
                                        'room': f"{self.courses[room1]['name']}/{self.courses[room2]['name']}",
                                        'instructor': self.teachers[teacher_id]["name"]
                                }

                                check_same_student[student_id]["sched"].append(student_schedule)

                        # Convert the dictionary into a list of programs
                        for student_id, schedule_details in check_same_student.items():
                                programs.append(schedule_details)

                        option = f"option {options_counter}"
                        formatted_data.append({"options": option, "programs": programs})

                return formatted_data
    
        def get_day_name(day):
                days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                # Ensure that the day value is a string representing a number
                try:
                        day_number = int(day)
                        if 1 <= day_number <= 6:
                                return days_of_week[day_number - 1]
                        else:
                                return "Invalid Day"
                except ValueError:
                        return "Invalid Day"
                
        def get_time(self, hour):
                start, end = hour
                s = self.convert_to_12_hour_format(start)
                e = self.convert_to_12_hour_format(end)
                time = f"{s}-{e}"
                return time

        def convert_to_12_hour_format(hour):
                if hour == 12:
                        return "12pm"  # Special case for 12pm
                elif hour > 12:
                        return f"{hour - 12}pm"
                else:
                        return f"{hour}am"