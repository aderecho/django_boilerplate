from django.urls import include, path

urlpatterns = [
    path("auth/", include("app.routes.auth")),
    path("posts/", include("app.routes.post")),
]
