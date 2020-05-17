from django.urls import path
from . import views
# Add your urlpatterns here

urlpatterns=[
    path('',views.diariesView,name='diaryView'),
    path('diary/new',views.newDiaryView,name='newDiaryView'),
    path('diary/<int:diary_pk>/entry/',views.entryView,name='entryView'),
    path('diary/entry/update/<int:rowId>',views.updateEntry,name='updateEntry'),
    path('diary/<int:diary_pk>/entry/new',views.createEntry,name='createEntry'),
    path("diary/delete/entry/<int:entryPk>/",views.deleteEntry,name='deleteEntry'),
    path("diary/<int:diary_pk>/entry/validate/",views.validate_serial,name='validate_serial')
]