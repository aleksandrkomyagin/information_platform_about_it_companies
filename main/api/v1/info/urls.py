"""URLs configuration of the 'info' endpoints of 'Api' app v1."""

from django.urls import path

from api.v1.info.views import InfoAPIView, search_services_companies

urlpatterns = [
    path("industries/", InfoAPIView.as_view(), name="industries_list"),
    path("service_categories/", InfoAPIView.as_view(), name="service_categories_list"),
    path("services/", InfoAPIView.as_view(), name="services_list"),
    path("cities/", InfoAPIView.as_view(), name="cities_list"),
    path(
        "search_services_companies/",
        search_services_companies,
        name="search_services_companies_list",
    ),
]
