
## Task

1. **Extract the Key:**
   - Using the wallet address, find the corresponding letter/number using the Asset ID.
   - The index begins with the first character of the wallet address (index 0).
   - The first three characters from the asset ID will constitute the key: **ZA2**.
   - Continue this process for all numbers from the asset ID to form a string of **9 characters/numbers** from the wallet address.

   **Key Generation:**
   - For the asset ID `720485937`, use the wallet address to derive additional characters/numbers, to get ZA2Q5OBZZ

2. **Encrypt the Note:**
   - Use the generated key to encrypt the message: **"Algorand uses Pure Proof of Stake Algorithm."** using SHA-256

3. **Perform the Transaction:**
   - Send an ALGO to the provided wallet address.
   - Include a note that contains the encrypted string.

## Implementation

1. Ensure you have the `algosdk` library installed:
   ```bash
   pip install algosdk
   ```

## Resourses
1. https://www.devglan.com/online-tools/hmac-sha256-online
