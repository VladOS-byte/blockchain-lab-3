# Setup
from web3 import Web3

def getLatestData(addr, abi):
	alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/5HKq7S1lnvTuNZGqkfocRIcd7BIcsGZ7"
	w3 = Web3(Web3.HTTPProvider(alchemy_url))
	# Set up contract instance
	contract = w3.eth.contract(address=addr, abi=abi)
	# Make call to latestRoundData()
	latestData = contract.functions.latestRoundData().call()[1]
	return latestData

alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/5HKq7S1lnvTuNZGqkfocRIcd7BIcsGZ7"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
  
# Print if web3 is successfully connected
print("Connection status: " + ("Connected" if w3.isConnected() else "Disconnected"))

latest_block = 0
# Get the latest block number
block = w3.eth.block_number

abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'

names = ['ETH/USD: $', 'LINK/ETH: E', 'USDT/ETH: E']

addresses = [w3.toChecksumAddress('0xf4030086522a5beea4988f8ca5b36dbc97bee88c'), # ETH/USDT
		w3.toChecksumAddress('0xdc530d9457755926550b59e8eccdae7624181557'), # LINK/ETH
		w3.toChecksumAddress('0xee9f2375b4bdf6387aa8265dd4fb8f16512a1d46')] # USDT/ETH

last_prices = [0, 0, 0]

fs = [lambda x: (x // 1000000) / 100, lambda x: (x / 1000000000000000000), lambda x: (x / 1000000000000000000)]

while True:
	if (block != latest_block):
		latest_block = block
		print('New block: ' + str(block))

		upd = False
		for i in range(0, len(addresses)):
			price = getLatestData(addresses[i], abi)
			if price != last_prices[i]:
				upd = True
				last_prices[i] = price
				print(names[i] + str(fs[i](price)))

		if not upd:
			print('No updates')

	# Get the latest block number
	block = w3.eth.block_number
