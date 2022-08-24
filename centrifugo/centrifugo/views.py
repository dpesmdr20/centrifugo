from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
import json
from typing import Dict, List
import logging
logger = logging.getLogger('django')
import requests


from django.conf import settings
import json
# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def generate_token(request):
    request_params = json.loads(request.body)
    token = jwt.encode({"sub": "","channels":request_params['channels']}, settings.CENTRIFUGO_SECRETS, algorithm="HS256")
    print("token",token)
    return JsonResponse({"token":token})

def get_headers() -> Dict:
    return {'Content-Type': 'application/json', 'Authorization': f'apikey {settings.CENTRIFUGO_API_KEY}'}

@csrf_exempt
def broadcast(request):
    request_params = json.loads(request.body)
    data: Dict = {"method": 'broadcast', "params": {"channels": request_params['channels'], "data": request_params['data']}}
    requests.post(headers=get_headers(), url=settings.CENTRIFUGO_URL, data=json.dumps(data))

@csrf_exempt
def publish(request):
    request_params = json.loads(request.body)
    print("request_params",request_params)
    data: Dict = {"method": "publish", "params": {"channel": request_params['channel'], "data": request_params['data']}}
    logger.info(f"Real time published {request_params['channel']}")
    requests.post(headers=get_headers(), url=settings.CENTRIFUGO_URL, data=json.dumps(data))
    return JsonResponse({"message":"published message"})
