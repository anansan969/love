x = input('do you love me?')
if x == 'yes':
	print('me too')
	y = input('how much?')
	if float(y) >= 100:
		print('love')
	if float(y) < 100:
		print('hmm')
if x == 'no':
	print('cry')
	y = input('why not?')
	if int(y) > 5:
		print('ok')
else:
	print('what?')


