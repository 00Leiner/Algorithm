class _days:
    def __init__(self, _days) -> None:
        self.days = _days
    
    def days_dictionary(self):
        list_of_days = list(self.days)
        day_index = set()
        for i in range(len(list_of_days)):
            first_day_index = i + 1
            second_day_index = ((first_day_index + 2) % len(list_of_days)) + 1
            day_index.add((first_day_index, second_day_index))
        return day_index