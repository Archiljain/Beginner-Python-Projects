🔐 Message Encryption & Decryption CLI Tool
This is a simple Python-based command-line interface (CLI) tool to encrypt (code) or decrypt (decode) secret messages using a custom algorithm.

📌 Features
Encode messages by scrambling words with added randomness.

Decode encrypted messages back to their original form.

Handles both short and long words differently for enhanced simplicity.

Great for basic practice in string manipulation and logic building.

🛠️ How It Works
🔒 Encryption Logic:
For words with 3 or more letters:

Adds 3 random characters at the start and end.

Moves the first letter to the end of the word.

For words with less than 3 letters:

Reverses the word.

🔓 Decryption Logic:
Reverses the process above to get the original message back.