from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Account

# List accounts
def list_account(request):
    accounts = Account.objects.all()
    return render(request, "account/list.html", {"accounts": accounts})

# Create account
def create_account(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if username and email and password:
            Account.objects.create(username=username, email=email, password=password)
            return redirect("account_list")
        else:
            return render(request, "account/create.html", {"error": "Invalid data"})

    return render(request, "account/create.html")

# Update account
def update_account(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if username and email and password:
            account.username = username
            account.email = email
            account.password = password
            account.save()
            return redirect("account_list")
        else:
            return render(request, "account/update.html", {"account": account, "error": "Invalid data"})

    return render(request, "account/update.html", {"account": account})

# Delete account
def delete_account(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == "POST":
        account.delete()
        return redirect("account_list")
    return render(request, "account/delete.html", {"account": account})

# Account details
def account_details(request, id):
    account = get_object_or_404(Account, id=id)
    return render(request, "account/details.html", {"account": account})
