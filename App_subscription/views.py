from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from App_auth.models import *
from App_subscription.models import *
from App_subscription.serializers import *
import stripe

# Create your views here.
class SubscriptionPlanList(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class SubscriptionPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class SubscriberList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubscriberModel.objects.all()
    serializer_class = SubscriberSerializer

class SubscriberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubscriberModel.objects.all()
    serializer_class = SubscriberSerializer

# Purchase
stripe.api_key = 'your_stripe_api_key'
class SubscriptionPurchase(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription_plan = serializer.validated_data['subscription_plan']

        try:
            # Create a Stripe customer
            customer = stripe.Customer.create(
                phone_number=request.user.phone_number,
                source=request.data['stripe_token'],
            )
            serializer.validated_data['stripe_customer_id'] = customer.id

            # Charge the customer for the subscription
            charge = stripe.Charge.create(
                customer=customer.id,
                amount=subscription_plan.price * 100,
                currency='usd',
                description=subscription_plan.name,
            )
            serializer.validated_data['payment_status'] = 'succeeded'
        except stripe.error.CardError as e:
            # The card has been declined
            serializer.validated_data['payment_status'] = 'failed'
            raise serializers.ValidationError('Your card was declined.')

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SubscriptionCancel(generics.DestroyAPIView):
    queryset = SubscriberModel.objects.all()
    serializer_class = SubscriberSerializer

    def perform_destroy(self, instance):
        # Cancel the customer's subscription in Stripe
        customer = stripe.Customer.retrieve(instance.stripe_customer_id)
        customer.cancel_subscription()
        instance.delete()

# Admin Withdraw
def withdraw_money(request, pk):
    # Get the subscriber from the database
    subscriber = get_object_or_404(Subscriber, pk=pk)

    # Charge the customer's subscription
    invoice = stripe.Invoice.create(
        customer=subscriber.stripe_customer_id,
        subscription=subscriber.stripe_subscription_id,
    )
    invoice.pay()

class SubscriberWithdraw(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        pk = request.data['id']
        withdraw_money(request, pk)
        return Response(status=status.HTTP_200_OK)
