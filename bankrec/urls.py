from django.urls import path
from .views import (
    HomePageView,
    BusinessListView,
    BusinessDetailView,
    TransactionListView,
    TransactionDetailView,
    PersonListView,
    PersonDetailView,
    BusinessActivityListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Business URLs
    path("businesses/", BusinessListView.as_view(), name="business_list"),
    path("businesses/<int:pk>/", BusinessDetailView.as_view(), name="business_detail"),
    path(
        "businesses/<int:business_id>/transactions/",
        TransactionListView.as_view(),
        name="transaction_list",
    ),
    path(
        "transactions/<int:pk>/",
        TransactionDetailView.as_view(),
        name="transaction_detail",
    ),
    # Person URLs
    path("persons/", PersonListView.as_view(), name="person_list"),
    path("persons/<int:pk>/", PersonDetailView.as_view(), name="person_detail"),
    # Business Activity URLs
    path(
        "business_activity_codes/",
        BusinessActivityListView.as_view(),
        name="business_activity_list",
    ),
]
