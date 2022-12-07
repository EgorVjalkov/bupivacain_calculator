from fetofactor import fetofactor_smpl

class FindCount:

	def __init__(self, dict, description):
		for k in dict:
			interpretation = dict[k]['inter']
			print(f'press "{k}" if {description} {interpretation}')
		while True:
			self.answer = input()
			if self.answer in dict:
				break
		self.count = dict[self.answer]['count']

class Patient:

	def __init__(self):
		self.patient_name = input('Имя?\n')
		self.height = int(input('Рост в см?\n')) / 100
		self.weight = int(input('Вес в кг?\n'))
		self.bmi = round(self.weight/pow(self.height, 2), 1)

		# bmi
		bmi_interpretation_dict = {
			18.5: {'inter': 'deficit', 'count': -1},
			25.0: {'inter': 'normal', 'count': -1},
			30.0: {'inter': 'overage', 'count': 0},
			35.0: {'inter': 'obesity 1', 'count': 1},
			40.0: {'inter': 'obesity 2', 'count': 2},
			100.0: {'inter': 'obesity 3', 'count': 3}
		}
		for k in bmi_interpretation_dict:
			if self.bmi < k:
				self.bmi_count = bmi_interpretation_dict[k]['count']
				self.bmi_interpretation = bmi_interpretation_dict[k]['inter']
				break

		fetus_weight_dict = {
			'b': {'inter': 'big (fetus weight > 4kg)', 'count': 1},
			'n': {'inter': 'normal (fetus weight > 2.5kg and < 4kg)', 'count': 0},
			's': {'inter': 'small (fetus weight < 2.5kg)', 'count': -1}
		}
		fetus = FindCount(fetus_weight_dict, 'fetus is')
		self.fetus = fetus.answer
		self.fetus_count = fetus.count

		bladder_condition = {
			'r': {'inter': 'raptured or oligohydramnios', 'count': 0},
			'n': {'inter': 'whole, no polyhydramnios', 'count': 0},
			'p': {'inter': 'whole, polyhydramnios', 'count': 1},
		}
		bladder = FindCount(bladder_condition, 'bladder is')
		self.bladder = bladder.answer
		self.bladder_count = bladder.count

		back_discomfort_dict = {
			'y': {'inter': 'discomfort lying on the back', 'count': 1},
			'n': {'inter': 'NOT discomfort lying on the back', 'count': 0}
		}
		back = FindCount(back_discomfort_dict, 'pregnant has')
		self.back_discomfort = back.answer
		self.back_discomfort_count = back.count

		print(self.bmi, self.bmi_count, self.bmi_interpretation)
		print(self.fetus, self.fetus_count)
		print(self.bladder, self.bladder_count)
		print(self.back_discomfort, self.back_discomfort_count)


a = Patient()
# #дискомфорт на спине
# back = input('дискомфорт на спине? (y/n)\n')
#
# def imt(PocT, Bec):
#
# imt_fact = imt(PocT, Bec)[2]
# feto_fact = fetofactor_smpl(big, aqua, more)
# sum = 3 + imt_fact + feto_fact
#
# if sum > 7: sum = 7
#
# if sum <= 3 and back == 'y':
# 	sum += 1
# 	back = 1
# else: back = 0
#
#
# print(imt_fact)
# print(feto_fact)
# print(sum)