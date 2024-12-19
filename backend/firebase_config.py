import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBFScWNzyoFu55-3XFo_CAFV31KPdBkA9Y",
    "authDomain": "minor-project-coffee-shop.firebaseapp.com",
    "databaseURL": "https://minor-project-coffee-shop-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "minor-project-coffee-shop",
    "storageBucket": "minor-project-coffee-shop.firebasestorage.app",
    "messagingSenderId": "430486438543",
    "appId": "1:430486438543:web:85495c698c7ca79f3626fa",
    "measurementId": "G-CBEKH2M6P5"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
