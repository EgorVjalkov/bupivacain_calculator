from bupik_data import bupik_dose


def round_PocT(PocT):
	for i in range(145, 180, 5):
		if PocT == i: return i
		elif PocT >= 180: return 180
		elif PocT <= 145: return 145
		elif PocT > i and PocT < (i+5):
			return (i+5)


def calc_bupik(x, factors):
	for i in bupik_dose:
		if x == i[0]:
			return i[factors]
			
#print(calc_bupik(155, 3))
