import os
import pickle
import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-f111e-default-rtdb.firebaseio.com/",
    'storageBucket':"facerecognitionattendanc-f111e.appspot.com"
})

# Specify the parent directory containing multiple folders
parentDir = 'Images/egs'

# Initialize lists to store image data and employee IDs
imgList = []
employeeIds = []

# Loop through each folder in the parent directory
for folderName in os.listdir(parentDir):
    folderPath = os.path.join(parentDir, folderName)  # Construct full path to the folder

    # Check if the path is a directory
    if os.path.isdir(folderPath):
        pathList = os.listdir(folderPath)  # List all files in the current folder
        # print(f"Processing folder: {folderPath}")

        # Filter out empty images and populate employeeIds
        for path in pathList:
            imgList.append(cv2.imread(os.path.join(folderPath, path)))
            # appending the id's into studentIds array and storing them
            employeeIds.append(os.path.splitext(path)[0])
            # os.path.join(folderPath, path) with this line creating a full path (for example Images/321654.png)
            # print(os.path.splitext(path)) -> print(os.path.splitext(path)[0])
            fileName = f'{folderPath}/{path}'
            # fileName variable holds the path for the image
            bucket = storage.bucket()
            # bucket variable now has access to our database storageBucket.
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)
print(employeeIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        if img is not None:
            img_rg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            try:
                encode = face_recognition.face_encodings(img_rg)[0]
                encodeList.append(encode)
            except IndexError:
                print(f"No face found in {path}")
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, employeeIds]

print(encodeListKnown)
print("Encoding Complete")
print("Writing Into File...")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()

print("File saved")