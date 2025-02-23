## Image Steganography Project 🖼️🔐
This project allows users to hide and retrieve secret messages within images using steganography. The encryption process embeds the message inside an image, while decryption extracts it using a passcode. The message length is stored automatically, ensuring accurate retrieval. It supports JPG & PNG formats with password protection for security.

# Installation & Requirements
Ensure you have Python installed, then install the required dependency:

bash
Copy
Edit
pip install opencv-python

# Usage Instructions
🔹 Encryption (Hiding a Message)
1️⃣ Run the encryption script:

bash
Copy
Edit
python encrypt.py
2️⃣ Enter the image path, secret message, and passcode.
3️⃣ The encrypted image will be saved as encryptedImage.jpg.

🔹 Decryption (Extracting the Message)
1️⃣ Run the decryption script:

bash
Copy
Edit
python decrypt.py
2️⃣ Enter the encrypted image path and passcode.
3️⃣ The hidden message will be displayed.

# Features
✅ Stores message length automatically for accurate decryption
✅ Passcode protection for added security
✅ Supports both JPG & PNG image formats
