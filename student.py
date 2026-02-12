# student.py will become my central controller class

from studenttools.grade import GradeCalculator
from studenttools.attendance import AttendanceTracker
from studenttools.report import  Performance_Analyzer 

class Student:
    def __init__(self, name, scores,days_present,total_days, attendance_records):
        self.name = name
        self.scores = scores
        self.days_present = days_present
        self.total_days = total_days
        self.attendance_records = attendance_records
        self.grade_calculator = GradeCalculator(scores)
        self.attendance_tracker = AttendanceTracker(days_present, total_days)

    def get_grade(self):
        return self.grade_calculator.get_letter_grade()

    def get_attendance_status(self):
        return self.attendance_tracker.attendance_status()

    def get_performance_summary(self):
        average_score = self.grade_calculator.calculate_average()
        attendance_percentage = self.attendance_tracker.attendance_percentage()
        performance_analyzer = Performance_Analyzer(average_score, attendance_percentage)
        return performance_analyzer.performance_summary()