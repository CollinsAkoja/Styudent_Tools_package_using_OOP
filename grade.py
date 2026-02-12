# here i will be writing my codes for the students grade structure

class GradeCAlculator:
    def __init__(self, score):
        self.score = scores
   
    def calculate_average(self):
        return sum(self.scores)/ len(self.scores)
    
    
    def get_letter_grade(self):
        avg = self.calculate_average()
        
        
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 45:
            return "D"
        else:
            return "F"
        