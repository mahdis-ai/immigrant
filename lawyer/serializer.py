from rest_framework import  serializers
from reservation.models import Applicant,Lawyer
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['username','visa_type']
