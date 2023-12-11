"""Views decorators of Companies endpoints for use in documentation."""

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status

from api.v1.companies.serializers import CompanyDetailSerializer, CompanySerializer
from api.v1.drf_spectacular.companies.examples import Response200CompaniesDetailExample
from api.v1.drf_spectacular.companies.serializers import Response400QueryParamSerializer
from api.v1.drf_spectacular.serializers import (
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)

COMPANIES_VIEW_DECORATORS = {
    "CompanyViewSet": extend_schema_view(
        list=extend_schema(
            tags=("companies",),
            responses={
                status.HTTP_200_OK: CompanySerializer,
                status.HTTP_400_BAD_REQUEST: Response400QueryParamSerializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        retrieve=extend_schema(
            tags=("companies",),
            responses={
                status.HTTP_200_OK: CompanyDetailSerializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
            examples=[
                Response200CompaniesDetailExample,
            ],
        ),
    ),
    "FavoriteAPIView": extend_schema_view(
        post=extend_schema(
            tags=("favorite",),
            request=None,
            responses={
                status.HTTP_201_CREATED: OpenApiResponse(),
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        delete=extend_schema(
            tags=("favorite",),
            responses={
                status.HTTP_204_NO_CONTENT: OpenApiResponse(),
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
