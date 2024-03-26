from flask import Flask, render_template, request, redirect, url_for
from web3 import Web3, HTTPProvider

app = Flask(__name__)
w3 = Web3(HTTPProvider('http://localhost:8545'))  # Update with your Ethereum node
contract_address = '0xYourContractAddressHere'
abi = []  # Your contract's ABI here

contract = w3.eth.contract(address=contract_address, abi=abi)

@app.route('/')
def index():
    return render_template('index.html')  # A simple HTML form for investments

@app.route('/invest', methods=['POST'])
def invest():
    amount = request.form.get('amount')
    if amount:
        tx = contract.functions.invest().transact({
            'from': w3.eth.accounts[0],  # Example: Using the first account
            'value': w3.toWei(amount, 'ether')
        })
        w3.eth.waitForTransactionReceipt(tx)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
