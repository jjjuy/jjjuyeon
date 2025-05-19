class Student:
    def __init__(self, name, student_id):
        self.name = name
        self._student_id = student_id
        self._korean_quiz = 0
        self._math_quiz = 0
        self._science_quiz = 0
        self._total_score = 0

    def __str__(self):
        avg_score = self.get_avg_score()
        return (f"이름: {self.name}, 학번: {self._student_id}, "
                f"국어: {self._korean_quiz}, 수학: {self._math_quiz}, 과학: {self._science_quiz}, "
                f"총점: {self._total_score}, 평균: {avg_score:.2f}")

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self._student_id

    def get_korean_quiz(self):
        return self._korean_quiz

    def get_math_quiz(self):
        return self._math_quiz

    def get_science_quiz(self):
        return self._science_quiz

    def set_korean_quiz(self, score):
        self._korean_quiz = score
        self._update_total()

    def set_math_quiz(self, score):
        self._math_quiz = score
        self._update_total()

    def set_science_quiz(self, score):
        self._science_quiz = score
        self._update_total()

    def get_total_score(self):
        return self._total_score

    def get_avg_score(self):
        return self._total_score / 3

    def _update_total(self):
        self._total_score = self._korean_quiz + self._math_quiz + self._science_quiz

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')

student = Student(name, student_id)

korean = int(input('학생의 국어 성적을 입력하세요 : '))
math = int(input('학생의 수학 성적을 입력하세요 : '))
science = int(input('학생의 과학 성적을 입력하세요 : '))
student.set_korean_quiz(korean)
student.set_math_quiz(math)
student.set_science_quiz(science)
print(student)
