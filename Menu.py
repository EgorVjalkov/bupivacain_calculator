class Menu:
    def __init__(self, topic='', variants=(), description=''):
        self.topic = topic
        self.variants = variants
        if self.variants:
            if type(self.variants) == dict:
                self.unique_answers_flag = True
            else:
                self.variants = dict(enumerate(self.variants, 1))
                self.unique_answers_flag = False

        self.description = description

    def print_a_topic(self):
        if self.topic:
            print(self.topic)

    def print_variants(self):
        if self.unique_answers_flag:
            print_variants = {print(f'нажмите "{k}" if {self.description} {self.variants[k]}') for k in self.variants}
        else:
            print_variants = {print(f'нажмите {k} - {self.variants[k]}') for k in self.variants}

    def get_user_answer(self):
        while True:
            try:
                answer = input(': ')
                if type(self.variants) == int:
                    answer = answer.replace(',', '.')
                    answer = float(answer)
                elif type(self.variants) == dict:
                    if self.unique_answers_flag:
                        answer = self.variants[answer]
                    else:
                        if 'enter' in self.variants[int(answer)]:
                            answer = input(': ')
                        else:
                            answer = self.variants[int(answer)]
                break
            except KeyError:
                print('*********ошибка ввода!*********')
            except ValueError:
                print('*********ошибка ввода!*********')

        return answer
