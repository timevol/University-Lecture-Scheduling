class LectureRoom:
    pass


class Department:

    str_DepartmentName = ""

    # list Of LectureRooms
    l_LectureRooms = []

    # List Of String AcedicianNames
    l_StrAcedemician = []

    def __init__(self, str_DepartmentName: str = "",
                 l_LectureRooms: list = [], l_StrAcedemician: list = []):

        self.str_DepartmentName = str_DepartmentName

        self.l_LectureRooms = l_LectureRooms

        self.l_StrAcedemician = l_StrAcedemician

    # add only one Acedimician
    def AddAcedemician(self, appendingAcedemician: str = ""):

        self.l_StrAcedemician.append(appendingAcedemician)

    # add acedemician fromList
    def AddAcedemicianFromList(self, listOfAcedemican: list = []):

        self.l_StrAcedemician.extend(listOfAcedemican)

    def AddLectureRoom(self, appendingLectureRoom: LectureRoom = None):

        self.l_LectureRooms.append(appendingLectureRoom)

    def AddLectureRoomFromList(self, listOfLectureRoom: list = []):

        self.l_LectureRooms.extend(listOfLectureRoom)

    def __del__(self):

        del self.str_DepartmentName
        del self.l_LectureRooms
        del self.l_StrAcedemician


def test():
    print("Department Test Running ...")


if __name__ == "__main__":
    test()
