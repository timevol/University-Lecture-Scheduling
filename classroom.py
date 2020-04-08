# TO-DO
## Class Parameters
### Classroom Code
### Classroom Capacity
### Exam Capacity
### Classroom Time From Minutes
### Classroom Begin Time
### Classroom End Time
### Classroom Type

# for LectureTime timedelta(0,0,0,0,minute,hour,0)
import datetime

class Classroom:

    str_classroomCode = ""
    classroomCapacity = 0
    classroomExamCapacity = 0
    timeClassroomFromMinute = 0
    classroomBeginTime = None
    classroomEndTime = None
    str_classroomType = ""

    def __init__(self, 
                 str_classroomCode: str = "",
                 classroomCapacity: int = 0,
                 classroomExamCapacity: int = 0,
                 timeClassroomFromMinute int = 0,
                 str_classroomType: str = ""):

                self.str_classroomCode = str_classroomCode
                self.classroomCapacity = classroomCapacity
                self.classroomExamCapacity = classroomExamCapacity
                self.timeClassroomFromMinute = timeClassroomFromMinute
                self.str_classroomType = str_classroomType 


    def setLectureClassroomBeginTime(self,hour:int = 0,minute:int = 0):

        self.classroomBeginTime = datetime.timedelta(0,0,0,0,minute,hour,0)
        self.classroomEndTime = self.classroomBeginTime + datetime.timedelta(0,0,0,0,self.timeClassroomFromMinute,0,0)
    
    def getLectureClassroomEndTime(self) -> datetime.timedelta:

        return self.classroomEndTime

    def __del__(self):

        del self.str_classroomCode
        del self.classroomCapacity
        del self.classroomExamCapacity
        del self.classroomBeginTime
        del self.classroomEndTime
        del self.str_classroomType

def test():
    print("Classroom Test Running")
    pass
    
if __name__ == "__main__":
    test()