from django.contrib import admin
from django.urls import path, include

# ovo mi liči na router (kako se mičemo kroz searchbar a vjerojatno i in-app)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
]
