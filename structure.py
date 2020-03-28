class LectureRoom:
    pass


class Departments:
    pass


class Sturcture:

    structureName = ""
    # listOfRooms
    l_LectureRooms = []
    # listOfDepartments
    l_Departments = []

    # initialize
    def __init__(self, structureName: str = "",
                 l_LectureRooms: list = [], l_departments: list = []):

        self.structureName = structureName
        self.l_LectureRooms = l_LectureRooms
        self.l_Departments = l_departments

    def AddLectureRooms(self, appendingRoom: LectureRoom):
        pass

    def AddDepartment(self, appendingDepartments: Departments):
        pass

    def CountOfLectureRoom(self) -> int:
        pass

    def CountOfDepartments(self) -> int:
        pass

    # for deleting using del Obj
    def __del__(self):
        del self.structureName
        del self.l_LectureRooms
        del self.l_Departments


def test():
    pass


if __name__ == "__main__":
    print("Structre Test running ...")
    test()
