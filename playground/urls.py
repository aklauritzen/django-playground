from django.contrib import admin
from django.urls import path

from projects.views import (
    project_detail_view,

    # TODO: Should be places in a seperate view
    home_view,
)

from accounts.views import (
    login_view,
    logout_view,
    register_view
)

from ideas.views import (
    ideas_view,
    idea_create_view,
)


urlpatterns = [
    path('', home_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('ideas/', ideas_view),
    path('create_idea/', idea_create_view),
    path('projects/<int:pk>/', project_detail_view),  # pk = primary key
    path('admin/', admin.site.urls),
]
