from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import usersSerializer
from .models import users, register, booking
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class printname(APIView):
    def post(self, request):
        print(request.data.get('name'))
        print('success')
        return Response(status=200)
    
class signup(APIView):
    def post(self, request,format=None):
        try:
            print(request.data['first_name'])
            new_data = users(first_name=request.data['first_name'], last_name=request.data['last_name'], phone=request.data['phone'],mail=request.data['mail'], pincode=request.data['pincode'], city=request.data['city'], street=request.data['street'], district=request.data['district'], state=request.data['state'], country=request.data['country'], password=request.data['password'])
            new_data.save()
            return Response(status=200)
        except:
            return Response(status=400)

class login(APIView):
    def post(self, request):
        try:
            print(request.data['mail'])
            print(request.data['password'])
            data = users.objects.get(mail=request.data['mail'], password=request.data['password'])
            print(data)
            if data:
                return Response(status=200)
            else:
                return Response(status=400)
        except:
            return Response(status=400)
        
class renter(APIView):
    def post(self, request):
        print(request.data['name'])
        new_data = register(name=request.data['name'], phoneNumber=request.data['phoneNumber'], email=request.data['email'], description=request.data['description'], smoking=request.data['smoking'], hobbies=request.data['hobbies'], address=request.data['address'], city=request.data['city'], district=request.data['district'], state=request.data['state'], country=request.data['country'], pincode=request.data['pincode'], adharNumber=request.data['adharNumber'], start=request.data['start'], end=request.data['end'])
        new_data.save()
        return Response(status=200)
    
class citylist(APIView):
    def get(self, request):
        cities = register.objects.values_list('city', flat=True).distinct()
        cities_list = list(cities)
        print(cities_list)
        serialized_cities = {
            'cities': cities_list
        }
        print(serialized_cities)
        return JsonResponse(serialized_cities)

class searchcity(APIView):
    def post(self, request):
        requested_city = request.data.get('location')
        print(requested_city)
        matching_data = list(register.objects.filter(city=requested_city).values())
        print(matching_data)
        return JsonResponse(matching_data, safe=False)

class details(APIView):
    def post(self, request):
        requested_name = request.data.get('name')
        print(requested_name)
        matching_data = list(register.objects.filter(name=requested_name).values())
        return JsonResponse(matching_data, safe=False)

class request(APIView):
    def post(self, request):
        name = request.data.get('name')
        phone = request.data.get('phoneNumber')
        purpose = request.data.get('purpose')
        to = request.data.get('to')
        status = "Pending"
        new_data = booking(name=name, phoneNumber=phone, purpose=purpose, status=status, to=to)
        new_data.save()
        return Response(status=200)
    
class getrequests(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        print(phone)
        data = booking.objects.filter(to=phone, status="Pending").values()
        setdata = list(data)
        return JsonResponse(setdata, safe=False)
    
class accept(APIView):
    def post(self, request):
        phone_number = request.data.get('phoneNumber')
        booking_to_update = booking.objects.get(phoneNumber=phone_number)
        booking_to_update.status = "accepted"
        booking_to_update.save()
        print("success")
        return Response(status=200)
    
class myrequests(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        data = list(booking.objects.filter(phoneNumber=phone).values())
        return JsonResponse(data, safe=False)
    
class getto(APIView):
    def post(self, request):
        to_list = request.data # Assuming 'to' is a list of phone numbers in the request data
        data = []
        for phone_number in to_list:
            queryset = register.objects.filter(phoneNumber=phone_number).values()  # Retrieve data as dictionaries
            data.extend(queryset)
        return Response(data, status=200)