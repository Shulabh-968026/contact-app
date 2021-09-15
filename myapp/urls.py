
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all_contacts,name='contacts'),
    path('add',views.index,name='index'),
    path('card/<int:id>/',views.contact_card,name='card'),
    path('delete/<int:id>/',views.delete_contact,name='delete'),
    path('<int:id>/',views.edit_contact,name='edit_contact'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('image/<int:id>/',views.change_photo,name='image'),
    path('change_image/<int:id>/',views.change_image,name='change_image'),
]