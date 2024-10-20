import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime

# Mpesa API credentials
consumer_key = 'YOUR_CONSUMER_KEY' #replace this with your consumer key
consumer_secret = 'YOUR_CONSUMER_SECRET'
shortcode = 'YOUR_SHORTCODE'
lipa_na_mpesa_online_passkey = 'YOUR_PASSKEY'
lipa_na_mpesa_online_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

# Generate Mpesa Access Token
def generate_token():
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return response.json()['access_token']

# Initiate Payment Request
def lipa_na_mpesa_online(phone_number, amount):
    access_token = generate_token()
    headers = { 'Authorization': f'Bearer {access_token}' }
    payload = {
        "BusinessShortCode": shortcode,
        "Password": lipa_na_mpesa_online_passkey,
        "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": shortcode,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your_callback_url.com/callback",  # Update with your callback URL
        "AccountReference": "HospitalPayment",
        "TransactionDesc": "Payment for Hospital Ticket"
    }
    response = requests.post(lipa_na_mpesa_online_url, json=payload, headers=headers)
    return response.json()

# Simulate Payment
if __name__ == "__main__":
    phone_number = '254712345678'  # This is an Example number
    amount = 1000  # Payment amount in KES
    payment_response = lipa_na_mpesa_online(phone_number, amount)
    print(payment_response)
