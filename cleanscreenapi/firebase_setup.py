import os
import json
import firebase_admin
from firebase_admin import credentials, auth

service_account_info = json.loads(os.getenv('FIREBASE_SERVICE_ACCOUNT'))

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None