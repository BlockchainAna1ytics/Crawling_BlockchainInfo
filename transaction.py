


import json
import sys
import urllib.request
import time
import csv
from bs4 import BeautifulSoup
import string
import decimal
from datetime import datetime
f = open('Gopax.txt', 'w')
tran1 = '[\n'
f.write(tran1)	
for i in range(0, 7):
	url = 'https://blockchain.info/rawaddr/'
	address = '1HwTDtzRtJSKvprwmAc2YBhRhbyT1CTbex?&offset=' #입금주소
	offset = i * 50
	url = url + address + str(offset)
	print(url)
	req = urllib.request.urlopen(url)
	res = req.read().decode()
	data = json.loads(res)
	txs = data["txs"]
	for j in txs:
		inputs = j["inputs"]
		out = j["out"]
		t_hash = j["hash"]
		output_price = ''
		input_text = ''
		output_text = ''
		if len(inputs) > 1:
			continue
		#print(total_inputs)
		for t in range(len(out)):
			print(out[t]["addr"])
			if out[t]["addr"] == '1HwTDtzRtJSKvprwmAc2YBhRhbyT1CTbex':
				output_price = out[t]["value"]
				break
		output_price = round(decimal.Decimal(output_price) * decimal.Decimal(0.00000001), 8)
		body = '{\n' + '"transID" : "'+ t_hash + '",\n"amount_BTC" : +'+ str(output_price) +'\n},\n'
		f.write(body)
		#wr.writerow([t_hash[3 * t], date[t], input_price[t], output_price, inputs, outputs])
	time.sleep(15)
tran2 = ']'
f.write(tran2)
	