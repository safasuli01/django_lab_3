from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import  *

#lab3:
# def index(request):
#     return render(request, 'index.html')
#
# # List accounts
# def list_account(request):
#     accounts = Account.objects.all()
#     return render(request, "account/list.html", {"accounts": accounts})
#
# # Create account
# def create_account(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#
#         if username and email and password:
#             Account.objects.create(username=username, email=email, password=password)
#             return redirect("account_list")
#         else:
#             return render(request, "account/create.html", {"error": "Invalid data"})
#
#     return render(request, "account/create.html")
#
# # Update account
# def update_account(request, id):
#     account = get_object_or_404(Account, id=id)
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#
#         if username and email and password:
#             account.username = username
#             account.email = email
#             account.password = password
#             account.save()
#             return redirect("account_list")
#         else:
#             return render(request, "account/update.html", {"account": account, "error": "Invalid data"})
#
#     return render(request, "account/update.html", {"account": account})
#
# # Delete account
# def delete_account(request, id):
#     account = get_object_or_404(Account, id=id)
#     if request.method == "POST":
#         account.delete()
#         return redirect("account_list")
#     return render(request, "account/delete.html", {"account": account})
#
# # Account details
# def account_details(request, id):
#     account = get_object_or_404(Account, id=id)
#     return render(request, "account/details.html", {"account": account})


#-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->
#lab4

def list_account(request):
    context = {}
    accounts = Account.list_account()
    context["accounts"] = accounts
    return render(request, "account/list.html", context)

def create_account(request):
    context = {}
    form = CreateAccount()
    context["form"] = form
    if request.method == "POST":
        form = CreateAccount(request.POST, request.FILES)
        if form.is_valid():
            accountobj = Account.create_account(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
                form.cleaned_data["photo"]
            )
            return redirect("accountob")
        else:
            context["error"] = form.errors
    return render(request, "account/create.html", context)

def update_account(request, id):
    context = {}
    try:
        accountobj = Account.objects.get(id=id)
        form = UpdateAccount(
            initial={
                "username": accountobj.username,
                "email": accountobj.email,
                "password": accountobj.password,
                "photo": accountobj.photo,
            }
        )
        if request.method == "POST":
            form = UpdateAccount(request.POST, request.FILES)
            if form.is_valid():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                photo = form.cleaned_data["photo"]
                if not password:
                    password = accountobj.password

                if not photo:
                    image = accountobj.photo

                account_url = Account.update_account(
                    id, username, email, password, photo
                )
                return redirect(account_url)
            else:
                context["error"] = form.errors

        context["form"] = form
        context["account"] = accountobj

    except Account.DoesNotExist:
        return HttpResponse("Not found", status=404)

    return render(request, "account/update.html", context)

def delete_account(request, id):
    try:
        if request.method == "POST":
            Account.delete_account(id)
            return JsonResponse({"success": True})
    except Account.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "Not found"}, status=404
        )
def account_details(request, id):
    context = {}
    try:
        accountobj = Account.details_account(id)
        context["account"] = accountobj
    except Account.DoesNotExist:
        return HttpResponse("Account not found", status=404)
    return render(request, "account/details.html", context)