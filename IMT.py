def imt(PocT, Bec):
	x = (Bec/(PocT / 100).__pow__(2)).__round__()
	if x < 25:
		return (x, 'норма', -1)
	elif x < 30:
		return (x, 'избыток', 0)
	elif x < 35:
		return (x, 'ожирение1', 1)
	elif x < 40:
		return (x, 'ожирение2', 2)
	else:
		return (x, 'ожирение3', 3)
