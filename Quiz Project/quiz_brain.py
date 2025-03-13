class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_num = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        q_num = self.question_num
        q_text = self.question_list[q_num].text
        q_answer = self.question_list[q_num].answer
        user_answer = input(f"Q.{q_num + 1}: {q_text}. (True/False): ")
        self.check_answer(user_answer, q_answer)
        self.question_num += 1

    def check_answer(self, u_answer, q_answer):
        q_num = self.question_num + 1
        if u_answer.lower() == q_answer.lower():
            print("You are right")
            self.score += 1
            print(f"Your score: {self.score}/{q_num}")
        else:
            print("You haven't got it")
            print(f"Your score: {self.score}/{q_num}")
        print("\n")
