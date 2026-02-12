#studenttools/performance.py

class Performance_Analyzer:
    def __init__(self,average_score, attendance_percentage):
        self.average_score = average_score
        self.attendance_percentage = attendance_percentage
        
        
    def performance_summary(self):
        if self.average_score >= 70 and self.attendance_percentage >= 75:
            return "Excellent Performance"
        elif self.average_score >= 50 and self.attendance_percentage >= 60:
            return "Satisfactory Performance"
        else:
            return "Needs Improvement"
         
    