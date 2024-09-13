import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-f111e-default-rtdb.firebaseio.com/"
})

ref = db.reference('Employees')

data = {
    # "10003":
    #     {
    #         "Name": "Cristiano Ronaldo",
    #         "Department": "Technical Support",
    #         "Starting_year": 2023,
    #         "Total_attendance": 0,
    #         "Last_attendance_time": "2024-08-01 10:15:00",
    #         "Phone_number": 929292929,
    #         "Email_address": "ronaldo7@gmail.com",
    #         "Employment_status": "Full-time",
    #         "Location": "KTM,Budhanilkanth"
    #     },
# "52436":
    #     {
    #         "Name": "Tanka",
    #         "Department": "accountent",
    #         "Starting_year": 2023,
    #         "Total_attendance": 0,
    #         "Last_attendance_time": "2024-08-01 10:15:00",
    #         "Phone_number": 929242929,
    #         "Email_address": "tank097@gmail.com",
    #         "Employment_status": "Full-time",
    #         "Location": "Lalitpur,Balkhu"
    #     },
    # "431453":
    #     {
    #         "Name": "Jiban ",
    #         "Department": "accountent",
    #         "Starting_year": 2023,
    #         "Total_attendance": 0,
    #         "Last_attendance_time": "2024-08-01 10:15:00",
    #         "Phone_number": 929242929,
    #         "Email_address": "jiban097@gmail.com",
    #         "Employment_status": "Full-time",
    #         "Location": "Lalitpur,Balkhu"
    #     },
    # "10004":
    #     {
    #         "Name": "Lionel Messi",
    #         "Department": "Software development",
    #         "Starting_year": 2023,
    #         "Total_attendance": 0,
    #         "Last_attendance_time": "2024-08-01 10:15:00",
    #         "Phone_number": 923392929,
    #         "Email_address": "messi10@gmail.com",
    #         "Employment_status": "Full-time",
    #         "Location": "KTM,Chapali"
    #     },
    # "10007":
    #     {
    #         "Name": "Emily Blunt",
    #         "Department": "Finance",
    #         "Starting_year": 2023,
    #         "Total_attendance": 0,
    #         "Last_attendance_time": "2024-08-01 10:15:00",
    #         "Phone_number": 929242929,
    #         "Email_address": "emily097@gmail.com",
    #         "Employment_status": "Full-time",
    #         "Location": "Lalitpur,Balkhu"
    #     },
    "10000":
        {
            "Name": "Ishwor shrestha",
            "Department": "BEIT",
            "Starting_year": 2023,
            "Total_attendance": 0,
            "Last_attendance_time": "2024-08-01 10:15:00",
            "Phone_number": 929242929,
            "Email_address": "ishwor097@gmail.com",
            "Employment_status": "Full-time",
            "Location": "Lalitpur,Balkhu"
        },

    "10001":
        {
            "Name": "Jiban chaudhary",
            "Department": "accountent",
            "Starting_year": 2023,
            "Total_attendance": 0,
            "Last_attendance_time": "2024-08-01 10:5:00",
            "Phone_number": 929242929,
            "Email_address": "jiban097@gmail.com",
            "Employment_status": "Full-time",
            "Location": "Lalitpur,Balkhu"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

print("Data added to database")
