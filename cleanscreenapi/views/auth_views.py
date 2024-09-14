from django.http import JsonResponse
from cleanscreenapi.firebase_setup import verify_firebase_token

def sign_up(request):
    return JsonResponse({'message': 'User signed up successfully'})

def sign_in(request):
    return JsonResponse({'message': 'User signed in successfully'})

def protected_view(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({'error': 'No token provided'}, status=401)

    id_token = auth_header.split('Bearer ')[1]
    decoded_token = verify_firebase_token(id_token)

    if decoded_token is None:
        return JsonResponse({'error': 'Invalid token'}, status=401)

    return JsonResponse({'message': 'This route is protected'})
