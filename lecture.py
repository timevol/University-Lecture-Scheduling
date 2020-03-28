
# for yearsOfLecture
from enum import Enum

# for LectureTime timedelta(0,0,0,0,minute,hour,0)
import datetime


class YearOfLecture(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6


class Lecture:
    str_lectureCode = ""
    str_lectureName = ""
    lecturePopulation = 0
    str_Acedimican = ""
    yearOflecture = YearOfLecture.FIRST
    bool_CanDivide = False
    timeLectureFromMinute = 0
    startTime = None
    finishTime = None

    def __init__(self,str_lectureCode: str = "",
                 str_lectureName: str = "", lecturePopulation: int = 0,
                 str_Acedimican: str = "",
                 yearOflecture: YearOfLecture = YearOfLecture.FIRST,
                 bool_CanDivide: bool = False,timeLectureFromMinute:int = 0):
    
        self.str_lectureCode = str_lectureCode
        self.str_lectureName = str_lectureName
        self.lecturePopulation = lecturePopulation
        self.str_Acedimican = str_Acedimican
        self.yearOflecture = yearOflecture
        self.bool_CanDivide = bool_CanDivide
        self.timeLectureFromMinute = timeLectureFromMinute

    def setLectureStartTime(self,hour:int = 0,minute:int = 0):

        self.startTime = datetime.timedelta(0,0,0,0,minute,hour,0)
        self.finishTime = self.startTime + datetime.timedelta(0,0,0,0,self.timeLectureFromMinute,0,0)
    
    def getLectureFinishTime(self) -> datetime.timedelta:

        return self.finishTime

        
    def __del__(self):
        
        del self.str_lectureCode
        del self.str_lectureName
        del self.lecturePopulation
        del self.str_Acedimican
        del self.yearOflecture
        del self.bool_CanDivide
        del self.timeLectureFromMinute
        del self.timeLectureFromMinute
        del self.startTime
        del self.finishTime

        

    

def test():
    pass
    

if __name__ == "__main__":
    test()
