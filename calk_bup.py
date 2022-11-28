from IMT import imt
from fetofactor import fetofactor_smpl
from bupik_data import bupik_dose

#имт
PocT = int(input('Рост в см?\n'))
Bec = int(input('Вес в кг?\n'))

#плод
big = input('крупный или многоплодие? (y/n)\n')
if big == 'n': big = input('маловесный? (s/n)\n')

#воды
if big == 's': 
    aqua = ''
    more = ''
else:
    aqua = input('плодный пузырь целый? (y/n)\n')
    if aqua == 'y': 
        more = input('многоводие? (y/n)\n') 
    else: more = ''

#дискомфорт на спине
back = input('дискомфорт на спине? (y/n)\n')

#предворителтный подсчет суммы
sum = 3 + imt(PocT, Bec)[2] + fetofactor_smpl(big, aqua, more)

#лимитирование
if sum > 7: sum = 7

#окончательный подсчет суммы
if sum <= 3 and back == 'y':
	sum += 1
	back = 1
else: back = 0

#округление роста
def round_PocT(PocT):
	for i in range(145, 180, 5):
		if PocT == i: return i
		elif PocT >= 180: return 180
		elif PocT <= 145: return 145
		elif PocT > i and PocT < (i+5):
			return (i+5)

#финишная функция
def calc_bupik(x, sum):
	for i in bupik_dose:
		if x == i[0]:
			return i[sum]

result = calc_bupik(round_PocT(PocT), sum)
print(f'\n{sum}')			
print(f'на боку: {result}\nсидя: {result + 0.2}')

