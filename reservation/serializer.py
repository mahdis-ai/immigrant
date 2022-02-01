from rest_framework import  serializers
from reservation.models import Lawyer
class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['first_name', 'last_name','reservation_schedule']

