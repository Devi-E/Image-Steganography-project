import cv2
import os
import struct

def create_lookup_table():
    return {chr(i): i for i in range(255)}

def encrypt_image(image_path, message, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image. Check the file path.")
        return
    
    d = create_lookup_table()
    rows, cols, _ = img.shape
    
    if len(message) + 4 > rows * cols:
        print("Error: Message too long for the given image.")
        return
    
    # Store message length in first 4 pixels (as 32-bit integer)
    message_length = len(message)
    length_bytes = struct.pack("I", message_length)  # Convert length to 4 bytes
    
    for i in range(4):
        img[i // cols, i % cols, 0] = length_bytes[i]
    
    for i, char in enumerate(message):
        img[(i + 4) // cols, (i + 4) % cols, 0] = d[char]  # Store in Red channel
    
    cv2.imwrite(output_path, img)  # Save as PNG to prevent compression artifacts
    os.system(f"start {output_path}")  # Open the image on Windows
    print("Encryption Successful! Encrypted image saved as", output_path)

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    output_path = "encryptedImage.png"  # Save as PNG
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    with open("password.txt", "w") as f:
        f.write(password)
    
    encrypt_image(image_path, msg, output_path)
