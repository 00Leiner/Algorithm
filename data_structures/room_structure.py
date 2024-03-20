class room:
    def __init__(self, rooms) -> None:
        self.rooms = rooms
        self.lec_room = set()
        self.lab_room = set()
        self.room_type_identification()

    def room_type_identification(self):
        for room in self.rooms:
            room_type = room['type'].lower()

            if room_type == 'laboratory':
                self.lab_room.add(room['_id'])
            elif room_type == 'lecture':
                self.lec_room.add(room['_id'])
            else:
                print(f"error in room_type_identification: {room}")

    def room_dictionary(self, course_type):
        c_type = course_type.lower()
        if c_type == "laboratory":
            return {(room, room2) for room in self.lab_room for room2 in self.lec_room}
        if c_type == "lecture":
            return {(room, room2) for room in self.lec_room for room2 in self.lec_room}
        print(f"error in room_dictionary: {c_type}")
