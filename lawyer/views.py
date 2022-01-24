from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lawyer.serializer import ApplicantSerializer
from  reservation.models import Applicant
# Create your views here.
@api_view()
def applicant_list(request):
    applicants=Applicant.objects.all()
    serializer=ApplicantSerializer(applicants)
    return Response(serializer.data)