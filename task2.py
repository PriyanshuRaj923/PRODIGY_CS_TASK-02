from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent overflow during addition
    
    # Add key to each pixel value and wrap around within the uint8 range
    encrypted_array = (img_array + key) % 256
    
    # Convert back to uint8
    encrypted_array = encrypted_array.astype('uint8')
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_path)

def decrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent underflow during subtraction
    
    # Subtract key from each pixel value and wrap around within the uint8 range
    decrypted_array = (img_array - key) % 256
    
    # Convert back to uint8
    decrypted_array = decrypted_array.astype('uint8')
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(output_path)

def swap_pixels(image_array):
    # Swap pixels pairwise for simplicity (just an example)
    swapped_array = image_array.copy()
    for i in range(0, image_array.shape[0] - 1, 2):
        for j in range(0, image_array.shape[1] - 1, 2):
            # Swap (i, j) with (i+1, j+1)
            temp = swapped_array[i, j].copy()
            swapped_array[i, j] = swapped_array[i+1, j+1]
            swapped_array[i+1, j+1] = temp
    return swapped_array

def encrypt_image_with_swapping(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent overflow during addition
    
    # Add key to each pixel value and wrap around within the uint8 range
    encrypted_array = (img_array + key) % 256
    
    # Swap pixels
    encrypted_array = swap_pixels(encrypted_array)
    
    # Convert back to uint8
    encrypted_array = encrypted_array.astype('uint8')
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_path)

def decrypt_image_with_swapping(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint16)  # Use uint16 to prevent underflow during subtraction
    
    # Swap pixels back (since we swapped pairwise, doing it again reverses it)
    decrypted_array = swap_pixels(img_array)
    
    # Subtract key from each pixel value and wrap around within the uint8 range
    decrypted_array = (decrypted_array - key) % 256
    
    # Convert back to uint8
    decrypted_array = decrypted_array.astype('uint8')
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(output_path)

# Example usage:
# Encrypt an image with pixel value manipulation only
encrypt_image(r'C:\Users\Priyanshu Raj\OneDrive\Pictures\evs project.jpg', 50, 'encrypted.jpg')
decrypt_image(r'encrypted.jpg', 50, 'decrypted.jpg')

# Encrypt an image with pixel value manipulation and swapping
encrypt_image_with_swapping(r'C:\Users\Priyanshu Raj\OneDrive\Pictures\evs project.jpg', 50, 'encrypted_swap.jpg')
decrypt_image_with_swapping(r'encrypted_swap.jpg', 50, 'decrypted_swap.jpg')
