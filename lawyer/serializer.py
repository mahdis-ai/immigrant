from rest_framework import  serializers
from reservation.models import Applicant,Lawyer
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['username', 'password','visa_type']
class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['first_name', 'last_name',]
