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