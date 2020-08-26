# Crawling_BlockchainInfo

Gaining Bitcoin Transaction information of address by Crawling [Blockchain.com](https://www.blockchain.com/explorer) or Using [API](https://www.blockchain.com/api) of Blockchain.com

Gained information will be saved as .csv file.  
Fields are TXID, Block Number, Time, input BTC, output BTC, inputs, outputs.  
Inputs and outputs fields will be formed like below.  
```  
[{address: "$address", BTC: "$amount_of_BTC BTC"}, {address: "$address", BTC: "$amount_of_BTC BTC"}]
```
## How to Use:zap:
1. Crawling from Blockchain.com.
    - Access the [Blockchain.com](https://www.blockchain.com/explorer).
    - Find address that you want to get transaction information.
    - Run crawling_blockinfo.py.
    - Enter the address.
    - Enter pages. 
    (Pages = number of transactions / 50)
  
2. Using API of Blockchain.com
    - Find address that you want to get transaction information.
    - Run crawling_blockapi.py.
    - Enter the address.
    - Enter pages.
    (Pages = number of transactions / 50)

## Requirements
1. Python 3
2. BeautifulSoup 4

## Notice
- Second way is much faster than first way but if you send too many request, they may prohibit you from using API for couple of days.
- If you want to use API without limitation, request for [API key](https://api.blockchain.info/customer/signup).
- Using Jupyter Notebook or Sublime Text is recommended. (PyCharm may not work with BeautifulSoup)
- If key 'addr' is not available in API, it will show as ' '.
