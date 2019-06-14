from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/',logout, name='logout'),
    path('add_skill/',CreateSkill.as_view(), name='add_skill'),
    path('skillsindex/',views.SkillsIndex.as_view(), name='skills_index'),
]