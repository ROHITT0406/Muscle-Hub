from rest_framework import serializers
from home.models import Contact,Plansdetails,Class

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plansdetails
        fields='__all__'
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields='__all__'
