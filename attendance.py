# for student attendance

class AttendanceTracker:
    def __init__(self, days_present, total_days):
        self.days_present = days_present
        self.total_days = total_days
        
    def attendance_percentage(self):
        return (self.days_present/ self.total_days)* 100
    
    def attendance_status(self):
        percentage = self.attendance_percentage()
        
        if percentage >= 75:
            return "Good standing"
        else:
            return "Low Attendance"
