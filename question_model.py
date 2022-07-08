class Question:
    def __init__(self, qText, qAnswer):
        self.text = qText
        self.answer = qAnswer

newQ = Question("something", "False")

print(newQ.text)