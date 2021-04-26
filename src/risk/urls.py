from django.urls import path, include


app_name = 'risk'

urlpatterns = [
    path('v1/', include('risk.v1.urls'))
]
