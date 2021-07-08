from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import userSerializer
from .models import User
from rest_framework import status


@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Connection Secure, Make API Calls"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_users(request):
    user = request.user.id
    serializer = userSerializer(user, many=True)
    return JsonResponse({'userdata': serializer.data}, safe=False, status=status.HTTP_200_OK)   

import json
from django.core.exceptions import ObjectDoesNotExist
@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_user(request):
    payload = json.loads(request.body)
    #user = request.user
    try:
        user = User.objects.create(
            username=payload["username"],
            password=payload["password"],
            email = payload["email"],
            phone = payload["phone"],
            class_level = payload["class_level"],
            user_type = payload["user_type"],
        ) 
        serializer = userSerializer()
        return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

