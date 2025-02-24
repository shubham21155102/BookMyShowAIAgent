from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET,require_POST
from  .models import CustomerTable
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@require_GET
def health_check(request):
    return JsonResponse({"status": "ok", "service": "accounts"})



# def register(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     phone_number = request.POST.get('phone_number')
#     address = request.POST.get('address')
#     preferences = request.POST.get('preferences')
#     print(username,password,phone_number,address,preferences)
#     return JsonResponse({"status": "ok", "message": "User registered successfully"})


# @csrf_exempt
# @require_POST
# def register(request):
#     data = json.loads(request.body.decode('utf-8'))
#     print(data)
#     username = data.get('username')
#     password = data.get('password')
#     phone_number = data.get('phone_number')
#     address = data.get('address')
#     preferences = data.get('preference')
#     # print(username,password,phone_number,address,preferences)
#     # return JsonResponse({"status": "ok", "message": "User registered successfully","data":{
#     #     "username":username,
#     #     "password":password,
#     #     "phone_number":phone_number,
#     #     "address":address,
#     #     "preferences":preferences
#     # }})
#     # interact with the database here
#     CustomerTable.objects.create(username=username, password=password, phone_number=phone_number, address=address, preferences=preferences)
#     return JsonResponse({"status": "ok", "message": "User registered successfully"})


@csrf_exempt
@require_POST
def register(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        username = data.get('username')
        password = data.get('password')
        phone_number = data.get('phone_number')
        address = data.get('address')
        preferences = data.get('preference') 

        # Basic validation
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required"}, status=400)
        # Check if user already exists
        if CustomerTable.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "User already exists"}, status=400)
        # Create user
        CustomerTable.objects.create(
            username=username,
            password=password,
            phone_number=phone_number,
            address=address,
            preferences=preferences
        )

        return JsonResponse({"status": "ok", "message": "User registered successfully"})

    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"status": "error", "message": "An unexpected error occurred"}, status=500)
    
    
@csrf_exempt
@require_POST
def login(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        username = data.get('username')
        password = data.get('password')

        # Basic validation
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required"}, status=400)
        # Check if user exists
        if not CustomerTable.objects.filter(username=username, password=password).exists():
            return JsonResponse({"status": "error", "message": "Invalid username or password"}, status=400)

        return JsonResponse({"status": "ok", "message": "Login successful"})

    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"status": "error", "message": "An unexpected error occurred"}, status=500)
    
    
@csrf_exempt
@require_POST
def update_partial_profile(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        username = data.get('username')
        password = data.get('password')
        phone_number = data.get('phone_number')
        address = data.get('address')
        preferences = data.get('preference') 

        # Basic validation
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required"}, status=400)
        #check if user exists
        if not CustomerTable.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "User does not exist"}, status=400)
        # Check if user is genuine
        if not CustomerTable.objects.filter(username=username, password=password).exists():
            return JsonResponse({"status": "error", "message": "Invalid username or password"}, status=400)
        # Update user
        if phone_number:
            CustomerTable.objects.filter(username=username).update(phone_number=phone_number)
        if address:
            CustomerTable.objects.filter(username=username).update(address=address)
        if preferences:
            CustomerTable.objects.filter(username=username).update(preferences=preferences)
        if password:
            CustomerTable.objects.filter(username=username).update(password=password)
        return JsonResponse({"status": "ok", "message": "Profile updated successfully"})
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"status": "error", "message": "An unexpected error occurred"}, status=500)
        