from django.contrib import admin
from django.urls import path
from vehiclesapp.views import home, create_view, list_view, editar, eliminar

urlpatterns = [
    path('admin/', admin.site.urls),

    # ESTA ES LA LISTA — DEBE TENER ESTE NAME
    path('', list_view, name="lista"),

    # Crear
    path('create/', create_view, name="crear"),

    # Editar
    path('update/<int:id>/', editar, name="editar"),

    # Eliminar
    path('delete/<int:id>/', eliminar, name="eliminar"),
]
