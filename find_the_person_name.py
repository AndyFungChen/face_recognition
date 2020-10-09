import os 
import face_recognition
from face_recognition.api import face_distance
#name+path1 is the photo want to recognition, path is the database
name = "--" #You can either use name+path1 to compound a path or copy full of the path into path1
path1 = "---"+name+".jpg"

path = "---"     #database of face
uk = face_recognition.load_image_file(path1)
uk_encode = face_recognition.face_encodings(uk)[0]
print(path1)

known_names=[] 
for image_name in os.listdir(path):
        load_image = face_recognition.load_image_file(path+image_name) 
        known_names.append(image_name.split(".")[0])
for i in range(len(known_names)):
    path2 = path+known_names[i]+".jpg"
    data = face_recognition.load_image_file(path2)
    
    data_encoding = face_recognition.face_encodings(data)[0]

    results = face_recognition.compare_faces([uk_encode], data_encoding, tolerance=0.6)
    
    if False in results:
        pass
    else:
        print(name+ " is " + known_names[i])
        print(path2)

