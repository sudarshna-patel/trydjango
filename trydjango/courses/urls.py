from django.urls import path
from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    # MyListView
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)

app_name = 'courses'
urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    # path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', MyListView.as_view(), name='courses-list'),
    path('', CourseListView.as_view(), name='courses-list'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]
