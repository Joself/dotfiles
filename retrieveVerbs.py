#!/usr/bin/env python3
import requests, bs4, re, shelve
master = {}
wordName = 'test'

res = requests.get('http://latindictionary.wikidot.com/index-verbs')
res.raise_for_status()
resSoup = bs4.BeautifulSoup(res.text, 'html.parser')

verbFile = shelve.open('/home/joseph/python/Verbs')
#master = verbFile['master']

for link in resSoup.findAll('a', attrs={'href': re.compile(r'verb:')}):
	words = []
	newRes = requests.get('http://latindictionary.wikidot.com' + link.get('href'))
	newRes.raise_for_status()
	curSoup = bs4.BeautifulSoup(newRes.text, 'html.parser')

	try:
		wordElements = curSoup.find('table', {'class': 'wiki-content-table'}).findAll('td')
		translation = str(curSoup.find('strong')).replace('<strong>', '').replace('</strong>', '')
		mainForms = str(curSoup.findAll('p')[1]).replace('<p><strong>Main forms</strong>: ', '').replace('</p>', '')
	except AttributeError:
		print(link)
		continue

	for i in wordElements:
		if str(i)[:4] + str(i)[-5:] == '<td></td>':
	 		words.append(str(i).replace('<td>', '').replace('</td>', ''))
		elif str(i)[:16] + str(i)[-5:] == '<td colspan=\"2\"></td>':
	 		words.append(str(i).replace('<td colspan=\"2\">', '').replace('</td>', ''))

	for i in range(49, 61):
		del words[i]
	for i in range(109, 121):
		del words[i]
	del words[131], words[131], words[135], words[136]

	master[wordName] = {'Present':
							{'Active':
								{'Indicative': [words[0], words[4], words[8], words[12], words[16], words[20]],
								'Subjunctive': [words[1], words[5], words[9], words[13], words[17], words[21]]},
							'Passive':
								{'Indicative': [words[2], words[6], words[10], words[14], words[18], words[22]],
								'Subjunctive': [words[3], words[7], words[11], words[15], words[19], words[23]]}},
						'Imperfect':
							{'Active':
								{'Indicative': [words[24], words[28], words[32], words[36], words[40], words[44]],
								'Subjunctive': [words[25], words[29], words[33], words[37], words[41], words[45]]},
							'Passive':
								{'Indicative': [words[26], words[30], words[34], words[38], words[42], words[46]],
								'Subjunctive': [words[27], words[31], words[35], words[39], words[43], words[47]]}},
						'Future':
							{'Active': [words[48], words[50], words[52], words[54], words[56], words[58]],
							'Passive': [words[49], words[51], words[53], words[55], words[57], words[59]]},
						'Perfect':
							{'Active':
								{'Indicative': [words[60], words[64], words[68], words[72], words[76], words[80]],
								'Subjunctive': [words[61], words[65], words[69], words[73], words[77], words[81]]},
							'Passive':
								{'Indicative': [words[62], words[66], words[70], words[74], words[78], words[82]],
								'Subjunctive': [words[63], words[67], words[71], words[75], words[79], words[83]]}},
						'Pluperfect':
							{'Active':
								{'Indicative': [words[84], words[88], words[92], words[96], words[100], words[104]],
								'Subjunctive': [words[85], words[89], words[93], words[97], words[101], words[105]]},
							'Passive':
								{'Indicative': [words[86], words[90], words[94], words[98], words[102], words[106]],
								'Subjunctive': [words[87], words[91], words[95], words[99], words[103], words[107]]}},
						'Future Perfect':
							{'Active': [words[108], words[110], words[112], words[114], words[116], words[118]],
							'Passive': [words[109], words[111], words[113], words[115], words[117], words[119]]},
						'Imperative':
							{'Active':
								{'Singular': words[120],
								'Plural': words[122]},
							'Passive':
								{'Singular': words[121],
								'Plural': words[123]}},
						'Infinitive':
							{'Active':
								{'Present': words[124],
								'Perfect': words[126],
								'Future': words[128]},
							'Passive':
								{'Present': words[125],
								'Perfect': words[127],
								'Future': words[129]}},
						'Participle':
							{'Active':
								{'Present': words[130],
								'Future': words[132]},
							'Passive':
								{'Perfect': words[131],
								'Future': words[133]}},
						'Gerund':
							{'Genitive': words[134],
							'Dative': words[135],
							'Accusative': words[136],
							'Ablative': words[138]},
						'Supine':
							{'Accusative': words[137],
							'Ablative': words[139]}}

	for i in master[wordName]:
		ijLen = 0

		for j in master[wordName][i]:
			if type(master[wordName][i][j]) == str:
				print(master[wordName][i][j])
				ijLen = ijLen + 1 + len(master[wordName][i][j])
			elif type(master[wordName][i][j]) == list:
				for k in master[wordName][i][j]:
					print(k)
			else:

				for k in master[wordName][i][j]:
					if type(master[wordName][i][j][k]) == str:
						print(master[wordName][i][j][k])
					else:

						for l in master[wordName][i][j][k]:
							print(l)
		if ijLen == 2 or ijLen == 4:
			master[wordName][i] = None

	break

# verbFile['master'] = master
# verbFile.close()