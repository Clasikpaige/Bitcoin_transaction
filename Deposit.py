from bitcoinlib.services.services import Service

# Set up the wallet (import using your private key)
wallet = Wallet.import_wallet("my_wallet", key=private_key)

# Create a transaction
transaction = wallet.send_to('destination_address', amount=0.001)  # Replace with the actual address and amount

# Print the transaction ID
print(f"Transaction ID: {transaction.txid}")

# Broadcast the transaction (this sends the transaction to the Bitcoin network)
service = Service()
service.broadcast(transaction)
