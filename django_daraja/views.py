# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_daraja.mpesa import utils

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CallbackData  # Import your model if you want to save the data to a database

import logging

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CallbackData



logger = logging.getLogger(__name__)


@csrf_exempt
def stk_push_callback(request):
    if request.method == 'POST':
        try:
            callback_data = json.loads(request.body.decode('utf-8'))
            logger.info(f"Received callback data: {callback_data}")
            CallbackData.objects.create(data=callback_data)
            return JsonResponse({'message': 'Callback received successfully'}, status=200)
        except json.JSONDecodeError:
            raw_data = request.body.decode('utf-8')  # Decode the raw body to a string
            print(f"Raw callback data received: {json.dumps({'raw_data': raw_data}, indent=4)}")  # Print in JSON format
            logger.error("Failed to decode JSON from callback data")
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

## The one above assumes amount and phone number are defined in the py server


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

'''
@csrf_exempt
def stk_push_callback(request):
    if request.method == 'POST':
        try:
            # Parse JSON payload
            data = json.loads(request.body)
            phone_number = data.get('LNM_PHONE_NUMBER')  # Map LNM_PHONE_NUMBER to phone_number
            total_amount = data.get('total_amount')      # Extract total_amount
            
            # Map total_amount to amount
            amount = total_amount

            # Validate required fields
            if not phone_number or not total_amount:
                return JsonResponse({
                    'status': 'error',
                    'message': 'LNM_PHONE_NUMBER and total_amount are required'
                }, status=400)

            # Validate amount
            try:
                amount = int(amount)  # Ensure amount is an integer
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Invalid total_amount'}, status=400)

            # STK Push Details
            account_reference = 'ABC001'
            transaction_desc = 'STK Push Description'
            callback_url = stk_push_callback_url

            # Call STK Push API
            r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

            return JsonResponse({
                'status': 'success',
                'message': r.response_description,
                'phone_number': phone_number,
                'amount': amount  # Return mapped amount for clarity
            })
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
'''


#def get_callback_data(request):
 #   callback_data = CallbackData.objects.all().values()
  #  print(list(callback_data))  # Print the callback data to the terminal
   # return JsonResponse(list(callback_data), safe=False)

from django.http import JsonResponse
from .models import CallbackData

def get_callback_data(request):
    try:
        latest_callback_data = CallbackData.objects.latest('timestamp')
        latest_callback_data_dict = {
            'id': latest_callback_data.id,
            'timestamp': latest_callback_data.timestamp,
            'data': latest_callback_data.data
        }
        print(latest_callback_data_dict)  # Print the latest callback data to the terminal
        return JsonResponse(latest_callback_data_dict, safe=False)
    except CallbackData.DoesNotExist:
        return JsonResponse({'error': 'No callback data found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


cl = MpesaClient()
stk_push_callback_url = 'https://65ba-105-163-158-23.ngrok-free.app/stk_push/callback/'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def index(request):

	return HttpResponse('Welcome to the home of daraja APIs')

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)

def stk_push_success(request):
	phone_number = config('LNM_PHONE_NUMBER')
	amount = 1
	account_reference = 'ABC001'
	transaction_desc = 'STK Push Description'
	callback_url = stk_push_callback_url
	r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)


def business_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Business Payment Description'
	occassion = 'Test business payment occassion'
	callback_url = b2c_callback_url
	r = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def salary_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Salary Payment Description'
	occassion = 'Test salary payment occassion'
	callback_url = b2c_callback_url
	r = cl.salary_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def promotion_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Promotion Payment Description'
	occassion = 'Test promotion payment occassion'
	callback_url = b2c_callback_url
	r = cl.promotion_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)
