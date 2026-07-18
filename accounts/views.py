from django.shortcuts import render
from django.http import JsonResponse
import json
import requests


# =========================
# الصفحات الأساسية
# =========================

def index(request):
    return render(request, 'accounts/index.html')


def about(request):
    return render(request, 'accounts/about.html')


def pricing(request):
    return render(request, 'accounts/pricing.html')


def second(request):
    return render(request, 'accounts/second.html')


def book(request):
    return render(request, 'accounts/book.html')

def protein(request):
    return render(request, 'accounts/protein.html')


def calories(request):
    return render(request, 'accounts/calories.html')
# =========================
# تحديد الدولة والعملة
# =========================

def proteinen(request):
    return render(request, 'accounts/proteinen.html')


def caloriesen(request):
    return render(request, 'accounts/caloriesen.html')




# =========================
# Webhook فواتيرك
# =========================

def paid_webhook(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            print("✅ Payment Data Received:", data)

            payment_status = data.get("status")

            if payment_status == "paid":

                print("✅ PAYMENT SUCCESS")

                return JsonResponse({
                    "status": "success"
                })

        except json.JSONDecodeError:

            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    return JsonResponse({
        "status": "received"
    }, status=200)
