from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Trainee
from account.models import Account
from track.models import Track


def trainee_list(request):
    context = {"trainees": Trainee.objects.all()}
    return render(request, "trainee/list.html", context)


def create_trainee(request):
    context = {
        "accounts": Account.objects.all(),
        "tracks": Track.objects.all()
    }
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        date_of_birth = request.POST.get("date_of_birth")
        account_id = request.POST.get("account_obj")
        track_id = request.POST.get("track_obj")

        if all([first_name, last_name, date_of_birth, account_id, track_id]):
            try:
                account = Account.objects.get(id=account_id)
                track = Track.objects.get(id=track_id)
                Trainee.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    account_obj=account,
                    track_obj=track
                )
                return redirect("trainee_list")
            except Account.DoesNotExist:
                context["error"] = "Account not found"
            except Track.DoesNotExist:
                context["error"] = "Track not found"
        else:
            context["error"] = "Invalid data"

    return render(request, "trainee/create.html", context)


def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    context = {
        "accounts": Account.objects.all(),
        "tracks": Track.objects.all(),
        "trainee": trainee
    }

    if request.method == "POST":
        trainee.first_name = request.POST.get("first_name", trainee.first_name)
        trainee.last_name = request.POST.get("last_name", trainee.last_name)
        trainee.date_of_birth = request.POST.get("date_of_birth", trainee.date_of_birth)

        try:
            trainee.account_obj = Account.objects.get(id=request.POST.get("account_obj"))
            trainee.track_obj = Track.objects.get(id=request.POST.get("track_obj"))
        except Account.DoesNotExist:
            return HttpResponse("Account not found", status=404)
        except Track.DoesNotExist:
            return HttpResponse("Track not found", status=404)

        trainee.save()
        return redirect("trainee_list")

    return render(request, "trainee/update.html", context)


def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    if request.method == "POST":
        trainee.delete()
        return redirect("trainee_list")

    context = {"trainee": trainee}
    return render(request, "trainee/delete.html", context)


def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    context = {"trainee": trainee}
    return render(request, "trainee/details.html", context)
