import re
import os
from bs4 import BeautifulSoup as bs

basepath = os.path.dirname(os.path.abspath(__file__))

# initialize list and dictionary for lines
all_lines = []
characters = {'ZACH': [], 'TAYLOR': [], 'SOOKIE': [], 'RORY': [], 'RICHARD': [], \
	'PARIS': [], 'MISS PATTY': [], 'MICHEL': [], 'MAX': [], 'LUKE': [], 'LORELAI': [], \
	'LOGAN': [], 'LANE': [], 'KIRK': [], 'JESS': [], 'JASON': [], 'JACKSON': [], \
	'EMILY': [], 'DEAN': [], 'CHRISTOPHER':[]}

# for each transcript, extract lines, remove speaker, and remove stage directions,
# then append to list
for i in range(1, 154):
	soup = bs(open(basepath+'/text/orig/ep{}.html'.format(i), encoding='windows-1252'), 'html.parser')

	script = soup.findAll('div', {'align': 'left'})

	lines = script[0].findAll(text=True)

	for line in lines:
		l = line.strip()
		l = re.sub(r"([\[][\w.,;!?\-' ]+[\]][ ]*)", '', l)
		pattern2 = re.compile("([A-Z ]+)([:][ ])([\w.,;!?\-'’ ]*)")
		m = pattern2.match(l)
		if m:
			if m.group(1) in characters.keys():
				characters[m.group(1)].append(m.group(3))
			else:
				pass
			all_lines.append(m.group(3))
		else:
			pass
	print('Episode {} done'.format(i))


# write to text files
with open(basepath+'/text/all-lines.txt', 'w') as f:
	for line in all_lines:
  		f.write('{}\n'.format(line))

for key in characters.keys():
	with open(basepath+'/text/{}.txt'.format(key), 'w') as f:
		for line in characters[key]:
			f.write('{}\n'.format(line))
