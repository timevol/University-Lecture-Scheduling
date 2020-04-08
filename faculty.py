# TO-DO
## Class Parameters
### Faculty Name
### Departments of Faculty
### Buildings of Faculty

class Faculty:

    str_faculty = ""
    l_departmentsOfFaculty = []
    l_buildingsOfFaculty = []

    def __init__(self, str_faculty: str = ""):

        self.str_faculty = str_faculty
        self. l_departmentsOfFaculty = []
        self.l_buildingsOfFaculty = []
    
    def addDepartment(self, departmentOfFaculty):

        self. l_departmentsOfFaculty.append(departmentOfFaculty)

    def addBuilding(self, buildingOfFaculty):

        self.l_buildingsOfFaculty.append(buildingOfFaculty)

    def __del__(self):

        del self.str_faculty = str_faculty
        del self. l_departmentsOfFaculty
        del self.l_buildingsOfFaculty


def test():
    print("Faculty Test Running")
    pass

if __name__ == "__main__":
    test()