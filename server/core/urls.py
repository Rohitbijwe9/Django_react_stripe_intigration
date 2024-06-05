from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project",
        default_version='1.0.0',
        description="API for all things ...",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user')),
    path('transaction/', include('transaction.urls', namespace='transaction')),

    path("", TemplateView.as_view(
            template_name="doc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api-doc",
    ),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path(
        "openapi/",
        schema_view.without_ui(cache_timeout=0),
        name='openapi-schema',
    ),
]
