from django.urls import path, include
import blango_auth.views

urlpatterns = [
  path("accounts/", include("django.contrib.auth.urls")),
  path("accounts/profile", blango_auth.views.profile, name="profile"),
]