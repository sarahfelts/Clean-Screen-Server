from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, auth

load_dotenv(dotenv_path='../.env')

service_account_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_PATH')

cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None