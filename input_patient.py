from IMT import imt
from fetofactor import fetofactor_smpl


PocT = int(input('Рост в см?\n'))
Bec = int(input('Вес в кг?\n'))

#плод
big = input('крупный или многоплодие? (y/n)\n')
if big == 'n': big = input('маловесный? (s/n)\n')
#воды
aqua = input('плодный пузырь целый? (y/n)\n')
if aqua == 'y': more = input('многоводие? (y/n)\n') 
else: more = ''
#дискомфорт на спине
back = input('дискомфорт на спине? (y/n)\n')


imt_fact = imt(PocT, Bec)[2]
feto_fact = fetofactor_smpl(big, aqua, more)
sum = 3 + imt_fact + feto_fact

if sum > 7: sum = 7

if sum <= 3 and back == 'y':
	sum += 1
	back = 1
else: back = 0


print(imt_fact)
print(feto_fact)
print(sum) 