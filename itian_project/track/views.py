from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Track

def track_list(request):
    context = {}
    tracks = Track.objects.all()
    context["tracks"] = tracks
    return render(request, "track/list.html", context)

def create_track(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            track = Track(name=name, description=description)
            track.save()
            return redirect("track_list")
        else:
            context["error"] = "Invalid data"
    return render(request, "track/create.html", context)

def update_track(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            track.name = name
            track.description = description
            track.save()
            return redirect("track_list")
        else:
            context = {"error": "Invalid data"}
            return render(request, "track/update.html", context)

    context = {"track": track}
    return render(request, "track/update.html", context)

def delete_track(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        track.delete()
        return redirect("track_list")

    context = {"track": track}
    return render(request, "track/delete.html", context)

def track_details(request, id):
    track = get_object_or_404(Track, id=id)
    context = {"track": track}
    return render(request, "track/details.html", context)
