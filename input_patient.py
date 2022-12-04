from fetofactor import fetofactor_smpl

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
		for k in fetus_weight_dict:
			description = fetus_weight_dict[k]['inter']
			print(f'press "{k}" if fetus is {description}')
		self.fetus = input()
		while True:
			if self.fetus in fetus_weight_dict:
				break
		self.fetus_count = fetus_weight_dict[self.fetus]['count']

		bladder_condition = {
			'r': {'inter': 'raptured or oligohydramnios', 'count': 0},
			'n': {'inter': 'whole, no polyhydramnios', 'count': 0},
			'p': {'inter': 'whole, polyhydramnios', 'count': 1},
		}
		for k in bladder_condition:
			description = bladder_condition[k]['inter']
			print(f'press "{k}" if fetal bladder is {description}')
		self.bladder = input()
		while True:
			if self.bladder in bladder_condition:
				break
		self.bladder_count = bladder_condition[self.bladder]['count']

		print(self.bmi, self.bmi_count, self.bmi_interpretation)
		print(self.fetus, self.fetus_count)
		print(self.bladder, self.bladder_count)


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