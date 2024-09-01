import os
import cv2
import face_recognition
import pickle

# Path to the images directory
images_path = 'Images'

# List to store the image paths
image_paths = os.listdir(images_path)

# Filter out non-image files
image_paths = [path for path in image_paths if path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

# List to store the image encodings and IDs
encode_list_known = []
employee_ids = []

print("Encoding Started")

for path in image_paths:
    # Construct the full path to the image
    full_path = os.path.join(images_path, path)

    # Load the image
    try:
        img = cv2.imread(full_path)
        if img is None:
            print(f"Error processing image: {full_path} - Image could not be loaded.")
            continue

        # Convert the image to RGB format
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Extract the face encoding
        encode = face_recognition.face_encodings(rgb_img)

        if not encode:
            print(f"Error processing image: {full_path} - No face detected.")
            continue

        # Append the encoding and ID to the lists
        encode_list_known.append(encode[0])
        employee_ids.append(os.path.splitext(path)[0])

    except Exception as e:
        print(f"Error processing image: {full_path} - {str(e)}")

print("Encoding Completed")

# Save the encodings and IDs to a file
encode_list_known_with_ids = (encode_list_known, employee_ids)
with open('EncodeFile.p', 'wb') as file:
    pickle.dump(encode_list_known_with_ids, file)

print("File Saved")