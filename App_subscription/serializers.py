from rest_framework import serializers
from .models import SubscriberModel, SubscriptionPlan
from App_auth.serializers import CompanySerializer

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    subscriber = CompanySerializer()
    subscription_plan = SubscriptionPlanSerializer()
    class Meta:
        model = SubscriberModel
        fields = '__all__'

