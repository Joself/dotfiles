#!/usr/bin/env python3
import requests, bs4, re, shelve

res = requests.get('http://latindictionary.wikidot.com/index-nouns')
res.raise_for_status()
resSoup = bs4.BeautifulSoup(res.text, 'html.parser')

nounFile = shelve.open('/home/joseph/python/Nouns')
master = nounFile['master']

for link in resSoup.findAll('a', attrs={'href': re.compile(r'noun:')}):
	words = []
	newRes = requests.get('http://latindictionary.wikidot.com' + link.get('href'))
	newRes.raise_for_status()
	curSoup = bs4.BeautifulSoup(newRes.text, 'html.parser')

	try:
		wordElements = curSoup.find('table', {'class': 'wiki-content-table'}).findAll('td')
	except AttributeError:
		print(link)
		continue

	for i in wordElements:
	 	if str(i)[:4] + str(i)[-5:] == '<td></td>':
	 		words.append(str(i).lstrip('<td>').rstrip('/<td>'))
	wordName = words[0] + ', ' + words[2]

	try:
		words[6]
	except IndexError:
		continue

	miscElements = curSoup.findAll('p')
	words.append(str(miscElements[0]).replace('<p><strong>', '').replace('</strong></p>', ''))

	classElements = str(miscElements[1]).split('\n')
	gender = classElements[1].replace('<strong>Gender</strong>: ', '').replace('<br/>', '')
	declension = classElements[2].replace('<strong>Declension</strong>: ', '').replace('</p>', '')

	try:
		master[declension][gender][wordName] = {}
	except KeyError:
		continue

	master[declension][gender][wordName]['Singular'] = {'Nominative': words[0],
														'Genitive': words[2],
														'Dative': words[4],
														'Accusative': words[6],
														'Ablative': words[8],
														'Vocative': words[10]}

	master[declension][gender][wordName]['Plural'] = {'Nominative': words[1],
														'Genitive': words[3],
														'Dative': words[5],
														'Accusative': words[7],
														'Ablative': words[9],
														'Vocative': words[11]}

	if words[0] == '':
		master[declension][gender][wordName]['Singular'] = None
	if words[1] == '':
		master[declension][gender][wordName]['Plural'] = None

	master[declension][gender][wordName]['Translation'] = words[12]

	nounFile['master'] = master

nounFile.close()