from django.urls import path
from App_subscription import views

urlpatterns = [
    path('subscription-plans/', views.SubscriptionPlanList.as_view(), name='subscription-plan-list'),
    path('subscription-plans/<int:pk>/', views.SubscriptionPlanDetail.as_view(), name='subscription-plan-detail'),
    path('subscribers/', views.SubscriberList.as_view(), name='subscriber-list'),
    path('subscribers/<int:pk>/', views.SubscriberDetail.as_view(), name='subscriber-detail'),
    path('purchase-payment/', views.SubscriptionPurchase.as_view(), name='payment'),
    path('purchase-cancel/', views.SubscriptionCancel.as_view(), name='payment-cancel'),
    path('withdraw-cash/', views.SubscriberWithdraw.as_view(), name='withdraw'),
]

# /subscription-plans/: List of subscription plans
# /subscription-plans/<pk>/: Detail view for a specific subscription plan
# /subscribers/: List of subscribers
# /subscribers/<pk>/: Detail view for a specific subscriber
