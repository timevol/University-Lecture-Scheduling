# TO-DO
## Class Parameters
### Name-Surname of Academician
### Department of Academician
### Lectures of Academician

class Academician:

    str_academicianNameSurname = ""
    str_departmentOfAcademician = ""
    l_lecturesOfAcademician = []

    def __init__(self,
                 str_academicianNameSurname: str = "",
                 str_departmentOfAcademician: str = "",): 

        self.str_academicianNameSurname = str_academicianNameSurname
        self.str_departmentOfAcademician = str_departmentOfAcademician
        self.l_lecturesOfAcademician = []

    # Using
    # academicians = {}
    # academicians["M. Emre Alpar"] = Academicians("M. Emre Alpar")
    # academicians["M. Emre Alpar"].addLecture("Microprocessors")   

    def addLecture(self, lectureOfAcademician):

        self.l_lecturesOfAcademician.append(lecturesOfAcademician)

    def __del__(self):

        del self.str_academicianNameSurname
        del self.str_departmentOfAcademician
        del self.l_lecturesOfAcademician

def test():
    print("Academician Test Running")
    pass

if __name__ == "__main__":
    test()