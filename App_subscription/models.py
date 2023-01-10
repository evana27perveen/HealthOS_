from django.db import models
from App_auth.models import CompanyModel

# Create your models here.
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}-৳{self.price} ({self.duration})"
    

class SubscriberModel(models.Model):
    subscriber = models.ForeignKey(CompanyModel, related_name='subscriber_company', on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, related_name='subscription_plan', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    is_subscribed = models.BooleanField(default=False)
