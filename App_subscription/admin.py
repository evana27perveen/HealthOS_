from django.contrib import admin
from .models import SubscriberModel, SubscriptionPlan

# Register your models here.
admin.site.register(SubscriberModel)
admin.site.register(SubscriptionPlan)

