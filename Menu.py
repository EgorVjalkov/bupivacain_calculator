class Menu:
    def __init__(self, question, variants=()):
        self.question = question
        self.question_dict = {int: f'{self.question}? Enter a num', str: f'{self.question}?'}

        self.variants = variants
        if self.variants:
            self.variants = dict(enumerate(self.variants, 1))

    def print_a_question(self):
        try:
            print(self.question_dict[type(self.variants)])
        except KeyError:
            print(self.question)

    def print_variants(self):
        print_variants = {print(f'press {k} - {self.variants[k]}') for k in self.variants}

    def get_user_answer(self):
        while True:
            try:
                answer = input(': ')
                if type(self.variants) == int:
                    answer = answer.replace('')
                    answer = float(answer)
                elif type(self.variants) == dict:
                    answer = self.variants[int(answer)]
                break
            except KeyError:
                print('*********input error!*********')
            except ValueError:
                print('*********input error!*********')

        return answer
