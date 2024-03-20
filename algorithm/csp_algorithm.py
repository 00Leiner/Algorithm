from constraints.validate_constraints import is_assignment_valid
from domain.assignment_domain import assignment_domain
from constraints.schedule_availability_constraints import schedule_availability_constraints
from utils.remote import remotes
from algorithm import csp_algorithm

class csp_algorithm:
    def __init__(self) -> None:
        ass = assignment_domain()
        self.domain_assignmnet = ass.assignment()
        self.availability = schedule_availability_constraints
        self._remotes = remotes()
        self.num_solutions = remotes.number_of_solution()
        self.csp_algorithm = csp_algorithm()

    def backtracking_search(self):
        solutions = []
        self.backtrack({}, solutions)
        format = self._remotes.data_format(solutions)
        return format

    def backtrack(self, schedule, solutions):
        if len(solutions) == self.num_solutions:
            return# Stop the search if the desired number of solutions is reached
        
        if len(schedule) == len(self.domain_assignmnet):
            # Solution found, append it to the list of solutions
            solutions.append(schedule.copy())  # Use copy to avoid modifying the original assignment
            return 
        
        for student_id in self.domain_assignmnet:
            for course_code in self.domain_assignmnet[student_id]['course']:
                 for teacher_id in self.domain_assignmnet[student_id]['teacher']:
                    for room_id_1, room_id_2 in self.domain_assignmnet[student_id]['room']:
                        for day1, day2 in self.domain_assignmnet[student_id]['day']:
                            for time1, time2 in self.domain_assignmnet[student_id]['time']:
                                if is_assignment_valid(student_id, course_code, teacher_id, room_id_1, room_id_2, day1, day2, time1, time2):
                                    schedule[student_id] = {
                                        'course': course_code,
                                        'teacher': teacher_id,
                                        'room': (room_id_1, room_id_2),
                                        'day': (day1, day2),
                                        'time': (time1, time2)
                                    }

                                    self.availability.update_schedule(student_id, teacher_id, room_id_1, room_id_2, day1, day2, time1, time2)
                                    # Recursively backtrack
                                    self.backtrack(schedule, solutions)

                                    # Backtrack if no solution found
                                    schedule.pop((student_id, course_code))  # Remove after assigning
                                    
                                    self.availability.undo_update_schedule(student_id, teacher_id, room_id_1, room_id_2, day1, day2, time1, time2)
