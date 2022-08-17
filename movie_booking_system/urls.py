"""movie_booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""''
from datetime import datetime
from django.contrib import admin
from django.urls import path, register_converter
from movies import views


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)


register_converter(DateConverter, 'date')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowView.as_view()),
    path('shows', views.ShowView.as_view()),
    path('shows/<date:given_date>',
         views.ShowView.as_view()),
    path('shows/<int:movie_id>',
         views.ShowView.as_view()),

]
