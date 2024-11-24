from django.db import models


# Create your models here.
class Person(models.Model):
    """
    represents an individual user or an accountant
    role:
    - individual: can only view and generate reports for their own transactions
    - accountant: can view and generate reports for linked individuals
    """

    ROLES = [("individual", "Individual"), ("accountant", "Accountant")]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BusinessActivity(models.Model):
    """
    Represents a business activity code provided by the IRS (e.g., for tax reporting)
    can be referred as NAICS codes
    """

    code = models.CharField(max_length=10, unique=True)  # The business activity code
    description = models.TextField()  # Description of the business activity

    def __str__(self):
        return f"{self.code}: {self.description}"


class Category(models.Model):
    """
    represents a financial category for transactions
    """

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Business(models.Model):
    """
    represents a business owned by a person
    """

    name = models.CharField(max_length=100)
    person = models.ForeignKey(
        Person, related_name="businesses", on_delete=models.CASCADE
    )
    industry = models.CharField(max_length=100)  # i.e: Restaurants, Constructions,etc.
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Business: {self.name}, Owner: {self.person.first_name}"


class BusinessActivityLink(models.Model):
    """
    Captures the many-to-many relationship between businesses and business activities codes (NAICS codes).
    """

    business = models.ForeignKey(
        Business, related_name="business_activities", on_delete=models.CASCADE
    )
    business_activity = models.ForeignKey(
        BusinessActivity, related_name="linked_businesses", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.business.name}: {self.business.industry} ({self.business_activity.code})"


class BusinessCategory(models.Model):
    """
    Captures the many-to-many relationship between businesses and categories.
    Specifies if a category is tax-deductible for a given business.
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    is_tax_deductible = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.business.name}: {self.category.name} (Tax Deductible: {self.is_tax_deductible})"


class TransactionEntry(models.Model):
    """
    represents a financial transaction record
    note:
    - debit = money coming out
    - credit = money coming in
    - check = checks written
    """

    TRANSACTION_TYPE = [
        ("credit", "Credit"),
        ("debit", "Debit"),
        ("check", "Check"),
    ]
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    account_last4 = models.CharField(max_length=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    business = models.ForeignKey(
        Business, related_name="transaction_entries", on_delete=models.CASCADE
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    # Additional fields for checks and debits
    check_number = models.CharField(max_length=20, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)  # For checks
    payee = models.CharField(max_length=100, blank=True, null=True)  # For debits

    def __str__(self):
        return (
            f"{self.business.name}-{self.transaction_type.capitalize()}: {self.amount}"
        )
