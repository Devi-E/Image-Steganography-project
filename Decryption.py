import cv2
import struct

def create_lookup_table():
    return {i: chr(i) for i in range(255)}

def decrypt_image(image_path, password):
    try:
        with open("password.txt", "r") as f:
            correct_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found.")
        return
    
    if password != correct_password:
        print("YOU ARE NOT authorized!")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image. Check the file path.")
        return
    
    c = create_lookup_table()
    rows, cols, _ = img.shape
    
    # Read message length from first 4 pixels
    length_bytes = bytearray()
    for i in range(4):
        length_bytes.append(img[i // cols, i % cols, 0])
    
    message_length = struct.unpack("I", length_bytes)[0]
    
    message = ""
    for i in range(message_length):
        message += c[img[(i + 4) // cols, (i + 4) % cols, 0]]
    
    print("Decrypted message:", message)

if __name__ == "__main__":
    image_path = input("Enter the path of the encrypted image: ")
    pas = input("Enter passcode for Decryption: ")
    
    decrypt_image(image_path, pas)
