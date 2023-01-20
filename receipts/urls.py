from django.urls import path
from receipts.views import (
    receipt_list,
    create_receipt,
    category_list,
    account_list,
)


urlpatterns = [
    path("accounts/", account_list, name="account_list"),
    path("categories/", category_list, name="category_list"),
    path("create/", create_receipt, name="create_receipt"),
    path("", receipt_list, name="home"),
]
