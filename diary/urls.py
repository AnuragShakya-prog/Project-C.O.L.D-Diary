from django.urls import path
from . import views
# Add your urlpatterns here

urlpatterns=[
    path('',views.diariesView,name='diaryView'),
    path('new',views.newDiaryView,name='newDiaryView'),
    path('<int:diary_pk>/entry/',views.entryView,name='entryView'),
    path('entry/update/<int:rowId>',views.updateEntry,name='updateEntry'),
    path('<int:diary_pk>/entry/new',views.createEntry,name='createEntry'),
    path("delete/entry/<int:entryPk>/",views.deleteEntry,name='deleteEntry'),
    path("<int:diary_pk>/entry/validate/",views.validate_serial,name='validate_serial')
]