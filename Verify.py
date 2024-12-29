from bitcoinlib.wallets import Wallet

# Load or create the wallet using the private key
private_key = "761f45f8bd42f016a51808b9898e2034e76394339b6e09135d1072a1d1fe4445"  # Replace with the private key from your file

wallet = Wallet.import_wallet("my_wallet", key=private_key)

# Get the associated address
address = wallet.get_key().address
print(f"Associated Address: {address}")

# Verify if this address matches the one you want to check (for example, you want to check if it's the correct wallet)
expected_address = "your_target_address_here"  # Replace with the address you're verifying

if address == expected_address:
    print("Private key matches the expected address.")
else:
    print("Private key does NOT match the expected address.")
