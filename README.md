# Crawling_BlockchainInfo

Gaining Bitcoin Transaction information of address by Crawling [Blockchain.com](https://www.blockchain.com/explorer) or Using [API](https://www.blockchain.com/api) of Blockchain.com

## How to Use
1. Crawling from Blockchain.com.
    - Access the [Blockchain.com](https://www.blockchain.com/explorer).
    - Find address that you want to get transaction information.
    - Copy the address.
    - Run crawling_blockchain.py.
  
2. Using API of Blockchain.com
    - Find address that you want to get transaction information.
    - Copy the address.
    - Run crawling_blockapi.py.

## Requirements
1. Python 3
2. BeautifulSoup 4

## Notice
- Second way is much faster than first way but if you send too many request, they may prohibit you from using API for couple of days.
- If you want to use API without limitation, you have to request for API key(https://api.blockchain.info/customer/signup).
- Using Jupyter Notebook or Sublime Text is recommended. (PyCharm may not work with BeautifulSoup)
