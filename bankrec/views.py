from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Business, TransactionEntry, Category, Person, BusinessActivity


class HomePageView(TemplateView):
    template_name = "bankrec/home.html"


class PersonListView(ListView):
    """
    A view class to display a list of the app users
    """

    model = Person
    template_name = "bankrec/person_list.html"
    context_object_name = "persons"


class PersonDetailView(DetailView):
    """
    A view class to display user data
    """

    model = Person
    template_name = "bankrec/person_detail.html"
    context_object_name = "person"


class BusinessActivityListView(ListView):
    """
    A view class to display a list of business activities and their NAICS codes
    """

    model = BusinessActivity
    template_name = "bankrec/business_activity_list.html"
    context_object_name = "activities"


class BusinessListView(ListView):
    """
    A view class to display a list of businesses
    """

    model = Business
    template_name = "bankrec/business_list.html"
    context_object_name = "businesses"


class BusinessDetailView(DetailView):
    """
    A view class to display the detail view for a business and their data
    """

    model = Business
    template_name = "bankrec/business_detail.html"
    context_object_name = "business"


class TransactionListView(ListView):
    """
    A view class to display a list of transactions
    """

    model = TransactionEntry
    template_name = "bankrec/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        business = get_object_or_404(Business, id=self.kwargs["business_id"])
        return TransactionEntry.objects.filter(business=business)


class TransactionDetailView(DetailView):
    """
    A view class to display detail information for a transaction
    """

    model = TransactionEntry
    template_name = "bankrec/transaction_detail.html"
    context_object_name = "transaction"
