"""
Basic review of OOP: 
Design an exam class 

"""

class Student(object):
    """ A class of students and their information. """

    def __init__(self, first_name, last_name, address):
        self.first_name = name 
        self.last_name = lname
        self.address = address

class Question(object):
    """ A class of questions and correct answers. """

    def __init__(self, question, correct_answer):
        self.question = question 
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question + ">")
        return answer == str(self.correct_answer)

class Exam(object): 
    """ A class of exams and questions."""

    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))
    
    def administer(self):

        score = 0.0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1.0  
        final_score = score / len(self.questions) * 100 
        return final_score


exam = Exam('midterm')
exam.add_question('what color is the sky?', 'blue')
exam.add_question('Matthew last name?', 'Weil')
exam.add_question("Boo last name?" 'Trelles')
exam.administer()


class StudentExam(object):

    def __init__(self, student, exam, ):
        pass 

    def take_test(self):
        pass 


