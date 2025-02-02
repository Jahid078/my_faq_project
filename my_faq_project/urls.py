from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faq_app.urls')),  # faq_app.urls ko include karna hai
]
