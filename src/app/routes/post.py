from django.urls import path
from app.controllers.post_controller import PostListCreateController, PostDetailController

urlpatterns = [
    path("", PostListCreateController.as_view(), name="post-list-create"),
    path("<int:id>/", PostDetailController.as_view(), name="post-detail"),
]
