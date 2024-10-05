from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod

# Sender's mnemonic phrase (replace with your actual mnemonic)
mnemonic_phrase = ""

# Convert the mnemonic to a private key
sender_private_key = mnemonic.to_private_key(mnemonic_phrase)
sender_address = account.address_from_private_key(sender_private_key)

print(f"Sender Address: {sender_address}")

# Receiver address
receiver_address = ""

# Initialize Algod client (replace with your credentials)
algod_token = ""
algod_address = "https://testnet-api.4160.nodely.dev"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Define the note (the encrypted message as per your challenge)
note = "".encode()

# Get transaction parameters
params = algod_client.suggested_params()

# Create a transaction (sending 1 Algo = 1000000 microAlgos)
txn = transaction.PaymentTxn(sender_address, params, receiver_address, 1000000, note=note)

# Sign the transaction with the private key
signed_txn = txn.sign(sender_private_key)

# Send the transaction
txid = algod_client.send_transaction(signed_txn)

print(f"Transaction ID: {txid}")
