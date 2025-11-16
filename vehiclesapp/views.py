from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import vehicle

def home(request):
    return render(request, "home.html")

def create_view(request):
    form = VehicleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("lista")

    return render(request, "create_view.html", {"form": form})

def list_view(request):
    context = {}
    context["dataset"] = vehicle.objects.all()
    return render(request, "list_view.html", context)

def eliminar(request, id):
    item = vehicle.objects.get(id=id)
    item.delete()
    return redirect("lista")

# 🔥🔥 ESTA ES LA FUNCIÓN QUE TE PEDÍS
def editar(request, id):
    item = vehicle.objects.get(id=id)

    if request.method == "POST":
        form = VehicleForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = VehicleForm(instance=item)

    return render(request, "editar.html", {"form": form})

