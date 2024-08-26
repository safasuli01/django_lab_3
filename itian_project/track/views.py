from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


#LAB 3
# def track_list(request):
#     context = {}
#     tracks = Track.objects.all()
#     context["tracks"] = tracks
#     return render(request, "track/list.html", context)
#
# def create_track(request):
#     context = {}
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         if name and description:
#             track = Track(name=name, description=description)
#             track.save()
#             return redirect("track_list")
#         else:
#             context["error"] = "Invalid data"
#     return render(request, "track/create.html", context)
#
# def update_track(request, id):
#     track = get_object_or_404(Track, id=id)
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         if name and description:
#             track.name = name
#             track.description = description
#             track.save()
#             return redirect("track_list")
#         else:
#             context = {"error": "Invalid data"}
#             return render(request, "track/update.html", context)
#
#     context = {"track": track}
#     return render(request, "track/update.html", context)
#
# def delete_track(request, id):
#     track = get_object_or_404(Track, id=id)
#     if request.method == "POST":
#         track.delete()
#         return redirect("track_list")
#
#     context = {"track": track}
#     return render(request, "track/delete.html", context)
#
# def track_details(request, id):
#     track = get_object_or_404(Track, id=id)
#     context = {"track": track}
#     return render(request, "track/details.html", context)
#-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->
#LAB 4

def track_list(request):
     context = {}
     tracks = Track.list_track()
     context["tracks"] = tracks
     return render(request, "track/list.html", context)

def create_track(request):
    context = {}
    form = CreateTrackModel()
    context = {"form": form}
    return render(request, "track/create.html", context)

def update_track(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)
        form = UpdateTrack(
            initial={
                "name": trackobj.name,
                "description": trackobj.description,
                "photo": trackobj.photo,
            }
        )

        if request.method == "POST":
            form = UpdateTrack(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data["name"]
                description = form.cleaned_data["description"]
                photo = form.cleaned_data["photo"]

                if not photo:
                    photo = trackobj.photo

                track_url = Track.update_track(id, name, description, photo)
                return redirect(track_url)
            else:
                context["error"] = form.errors

        context["form"] = form
        context["track"] = trackobj
    except Track.DoesNotExist:
        return HttpResponse("Track not found", status=404)

    return render(request, "track/update.html", context)
