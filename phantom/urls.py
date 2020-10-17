from django.contrib import admin
from django.urls import path

from projects.views import (
    project_detail_view,

    # TODO: Should be places in a seperate view
    home_view,
    about_view,
    contact_view
)

from ideas.views import (
    ideas_view,
    idea_create_view,
)


urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('ideas/', idea_create_view),
    path('projects/<int:pk>/', project_detail_view),  # pk = primary key
    path('admin/', admin.site.urls),
]
