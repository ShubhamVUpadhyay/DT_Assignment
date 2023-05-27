from django.urls import path
from myapp import views

urlpatterns = [
    path('api/v3/app/events', views.create_event, name='create_event'),
    path('api/v3/app/events/<int:event_id>', views.get_update_delete_event, name='get_update_delete_event'),
]
