"""
URL configuration for the src project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Examples:
- Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

- Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

- Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect root URL to 'projects/'
    path('', RedirectView.as_view(url='projects/')),

    # Include URLs for the 'issue_tracking' app
    path('projects/', include('issue_tracking.urls')),

    # Include URLs for the 'account' app
    path('account/', include('account.urls')),

    # Admin panel URL
    path('admin/', admin.site.urls),
]
