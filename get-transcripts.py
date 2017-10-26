import time
import os
import configparser
from urllib.request import urlopen

basepath = os.path.dirname(os.path.abspath(__file__))

baseurl = 'https://crazy-internet-people.com/site/gilmoregirls/pages/'

ep = 1
for i in range(1, 8):
	if i == 1:
		for j in range(1, 22):
			site = urlopen(baseurl+'s{}/s{}s/{}.html'.format(i, i, ep)).read()
			with open(basepath+'/text/orig/ep{}.html'.format(ep), 'wb') as f:
				f.write(site)
			print('Episode {} done'.format(ep))
			ep += 1
			time.sleep(10)
	else:
		for j in range(1, 23):
			site = urlopen(baseurl+'s{}/s{}s/{}.html'.format(i, i, ep)).read()
			with open(basepath+'/text/orig/ep{}.html'.format(ep), 'wb') as f:
				f.write(site)
			print('Episode {} done'.format(ep))
			ep += 1
			time.sleep(10)
			