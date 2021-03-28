class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
            
        self.questionIndex += 1
    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(
                100, '*'))

                
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            self.displayProgress()
        else:
            self.displayProgress()
            self.displayQuestion()

    


q1 = Question('en iyi programlama dili hangisidir ?',
              ['C#', 'python', 'javascript', 'java'], 'C#')
q2 = Question('en popüler programlama dili hangisidir ?',
              ['python', 'javascript', 'C#', 'java'], 'C#')
q3 = Question('en çok kazandıran programlama dili hangisidir ?',
              ['C#', 'javascript', 'java', 'python'], 'C#')
q4 = Question('en çok sevilen programlama dili hangisidir ?',
              ['C#', 'javascript', 'java', 'python'], 'C#')
q5 = Question('en kolay programlama dili hangisidir ?',
              ['C#', 'javascript', 'java', 'python'], 'C#')

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.loadQuestion()
