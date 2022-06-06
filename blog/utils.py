import os
from pathlib import Path
from dotenv import load_dotenv
from web3 import Web3

env_path =os.getenv('ENVPATH')

ADDRESS = os.getenv('ADDRESS')
KEY = os.getenv('KEY')

def sendTransactionAndGetTxId(message):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/48c5f0ed484d4cc8a1ebf93f70c8ef08'))
    address = ADDRESS
    privateKey = KEY
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "ether")
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId