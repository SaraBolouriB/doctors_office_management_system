from user_account.models import *
from user_account.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

INVALID_DATA = status.HTTP_400_BAD_REQUEST
CREATED = status.HTTP_201_CREATED
SUCCEEDED_REQUEST = status.HTTP_200_OK

@api_view(['POST'])
def following(request):

    if request.method == 'POST':
        data = request.data
        favoriteObj = favoriteSerializer(data=data)

        if favoriteObj.is_valid():
            favoriteObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(favoriteObj.errors, status=INVALID_DATA)

@api_view(['POST'])
def comment(request):

    if request.method == 'POST':
        data = request.data
        commentObj = commentSerializer(data=data)

        if commentObj.is_valid():
            commentObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(commentObj.errors, status=INVALID_DATA)
        
@api_view(['GET'])
def search(request, keyword):

    if request.method == "GET":

        if keyword.isdigit():
            try:
                output = doctor.objects.get(dNumber=int(keyword))
                _output = doctorSerializer(output)
                return Response(_output.data, status=SUCCEEDED_REQUEST)
            except ObjectDoesNotExist:
                return Response("Not Found", status=SUCCEEDED_REQUEST)
                
        else:
            output = doctor.objects.filter(name__contains=keyword).all()
            _output = doctorSerializer(output, many=True)
            if not _output.data:
                return Response("Not Found", status=SUCCEEDED_REQUEST)
            return Response(_output.data, status=SUCCEEDED_REQUEST)

@api_view(['POST'])
def set_appointment(request):
    
    if request.method == 'POST':
        appointment = request.data
        appointmentObj = appointmentSerializer(data=appointment)

        if appointmentObj.is_valid():
            appointmentObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(appointmentObj.errors, status=INVALID_DATA)

@api_view(['GET'])
def show_times(request, day, date, doctorID):

    if request.method == 'GET':
        doctor_times = working_time.objects.filter(day=day, doctor_id=doctorID).all()
        appointment_times = appointment.objects.filter(date=date, doctor_id=doctorID).all()

        suggestion_times = []
        for dt in doctor_times:
            dtime = dt.start_time
            for at in appointment_times:
                atime = at.time
                if dtime != atime:
                    suggestion_times.append(dtime)

        return Response(suggestion_times, status=SUCCEEDED_REQUEST)