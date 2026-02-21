class Grade:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value > 100 or value < 0:
            raise ValueError(f"{self.private_name} must be between 0 and 100")
        else:
            setattr(obj, self.private_name, value)

class Student:
    math_grade = Grade()
    science_grade = Grade()
    def __init__(self, math_grade, science_grade):
        self.math_grade = math_grade
        self.science_grade = science_grade

if __name__ == "__main__":
    try:
        s = Student(85, 90)
        assert s.math_grade == 85
        assert s.science_grade == 90
        
        s.math_grade = 100
        assert s.math_grade == 100
        
        try:
            s.math_grade = 101
            print("Failed to catch > 100")
        except ValueError:
            pass
            
        try:
            s.science_grade = -1
            print("Failed to catch < 0")
        except ValueError:
            pass

        try:
            s.math_grade = "A"
            print("Failed to catch non-int")
        except ValueError:
            pass

        print("Verification successful")
    except AssertionError:
        print("Verification failed: Values not stored correctly")
    except Exception as e:
        print(f"An error occurred: {e}")