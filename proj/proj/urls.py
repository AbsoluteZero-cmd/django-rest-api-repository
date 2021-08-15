from django.conf.urls import url
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new


urlpatterns = [
    url('social/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api/', include('api.urls', namespace='api')),
    path('answers/', include('answers.urls', namespace='answers')),
    path('ratings/', include('ratings.urls', namespace='ratings')),
    path('', include('questions.urls', namespace='questions')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
