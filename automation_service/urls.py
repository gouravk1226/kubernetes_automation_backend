from django.urls import path

from automation_service.views import ProcessRequestView

urlpatterns = [
    path("launch", ProcessRequestView.as_view(), name="launch kubernetes"),

]