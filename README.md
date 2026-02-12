# Styudent_Tools_package_using_OOP



```
# Styudent Tools Package Using OOP

A Python package built using Object-Oriented Programming principles to manage student-related tasks such as grade calculation, attendance tracking, and performance summaries.
```
```
This project demonstrates modular programming and clean class design using Python.
```
---

## Features

- Student class for managing student details
- Grade calculation module
- Attendance tracking system
- Performance summary generation
- Modular OOP-based structure
- Easy to import into other Python projects

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## Project Structure

```

Styudent_Tools_package_using_OOP/
│
├── studenttools/
│   ├── __init__.py
│   ├── grade.py
│   ├── attendance.py
│   ├── performance.py
│
├── main.py
└── README.md

```

---

## Installation

1. Clone the repository:

```

git clone [https://github.com/CollinsAkoja/Styudent_Tools_package_using_OOP.git](https://github.com/CollinsAkoja/Styudent_Tools_package_using_OOP.git)

```

2. Navigate into the project directory:

```

cd Styudent_Tools_package_using_OOP

```

3. Run the main script:

```

python main.py

````

---

## Usage Example

```python
from studenttools.grade import GradeCalculator
from studenttools.attendance import AttendanceTracker
from studenttools.performance import PerformanceSummary

# Example usage
grades = GradeCalculator([70, 85, 90])
average = grades.calculate_average()
print("Average Score:", average)

attendance = AttendanceTracker(30, 27)
print("Attendance Percentage:", attendance.calculate_percentage())

performance = PerformanceSummary(average)
print("Performance Grade:", performance.get_performance_level())
````

---

## Learning Objectives

This project helps you understand:

* How to build Python packages
* How to structure modular programs
* Encapsulation and class design
* Reusability of code using imports

---

## Contributing

Feel free to fork this repository and improve the project.
Pull requests are welcome.

---

## License

 MIT License .

```
```
