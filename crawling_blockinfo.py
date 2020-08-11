import sys
import urllib.request
import csv
from bs4 import BeautifulSoup
import string
import decimal
f = open('Gopax.csv', 'w', newline= '', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['tx', 'block', 'time', 'input_BTC', 'output_BTC', 'fee_BTC', 'inputs', 'outputs'])
for a in range(1, 61):
	url = "https://www.blockchain.com/btc/address/1HwTDtzRtJSKvprwmAc2YBhRhbyT1CTbex?page="
	url = url + str(a)
	req = urllib.request.urlopen(url)
	res = req.read()
	url1 = 'https://www.blockchain.com/btc/tx/'
	bitinfourl = 'https://www.bitinfocharts.com/bitcoin/tx/'
	print(url)
	soup = BeautifulSoup(res, 'html.parser')
	k = []
	t_hash = []
	input_price = []
	date = []
	fee = []
	block = []
	for div_tag in soup.find_all('div', class_ = 'ccso3i-0 bmbfXL'):
		for a_tag in div_tag.find_all("a", class_ = 'sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO'):
			t_hash.append(a_tag)

	for div_tag in soup.find_all('div', class_ = 'kad8ah-0 kKDjc'):
		for span_tag in div_tag.find_all('span', class_ = 'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'):
			date.append(span_tag)

	for div_tag in soup.find_all("div", class_ = 'ge5wha-1 hdwAPC'):
		for span_tag in div_tag.find_all("span", class_ = 'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'):
			input_price.append(span_tag)

	for div_tag in soup.find_all("div", class_='sc-19pxzmk-0 lhmncg'):
		for span_tag in div_tag.find_all("span", class_='sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'):
			k.append(span_tag)
		for a_tag in div_tag.find_all("a", class_='sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO'):
			k.append(a_tag)

	for div_tag in soup.find_all('div', class_ = "kad8ah-1 giMhWw"):
		for span_tag in div_tag.find_all('span', class_ = 'sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg'):
			fee.append(span_tag)



	t_hash = [each_line.get_text().strip() for each_line in t_hash[:50]]
	input_price = [each_line.get_text().strip() for each_line in input_price[:50]]
	k = [each_line.get_text().strip() for each_line in k[:50]]
	fee = [each_line.get_text().strip() for each_line in fee[:50]]
	date = [each_line.get_text().strip() for each_line in date[:50]]

	for i in range(0, 30):
		if i < len(t_hash):
			if t_hash[i] == '':
				del t_hash[i]
		if i < len(k):
			if k[i] == '':
				del k[i]

	for i in range(0, 5): 
		url2 = url1 + t_hash[3 * i]
		if a == 24 and i == 4:
			url2 = url1 + t_hash[3 * i - 1]
		print(url2)
		req = urllib.request.urlopen(url2)
		res = req.read()
		soup = BeautifulSoup(res, 'html.parser')
		for div_tag in soup.find_all('div', class_ = "sc-8sty72-0 kcFwUU"):
			for a_tag in div_tag.find_all('a', class_ = 'sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO'):
				block.append(a_tag)

	block = [each_line.get_text().strip() for each_line in block[:50]]
	
	print(t_hash)
	print(date)
	print(input_price)
	print(k)
	print(fee)
	#print(block)

	for t in range(0, 5):
		if t == 4 and a == 13:
			break
		if t == 3 and a == 24:
			break
		output1 = k[4 * t + 1].split()
		output2 = k[4 * t + 2].split()
		input_1 = input_price[t].split()
		fee_1 = fee[2 * t].split()
		output_price = str(decimal.Decimal(output1[0]) + decimal.Decimal(output2[0]))
		inputs = '[{address: "'+ t_hash[3 * t + 1] + '", BTC: "' + input_price[t] + '"}]'
		outputs = '[{address: "'+ k[4 * t] + '", BTC: "' + k[4 * t + 1] + '"}, {address: "'+ k[4 * t + 3] + '", BTC: "' + k[4 * t + 2] + '"}]'
		wr.writerow([t_hash[3 * t], block[t], date[t], input_1[0], output_price, fee_1[0], inputs, outputs])
