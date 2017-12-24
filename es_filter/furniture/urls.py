from django.conf.urls import url
from .views import home_view, filtered_furnitures, get_furniture_filters

urlpatterns = [
    url(r'^home/$', home_view, name='home_view'),
    url(r'^filters$', get_furniture_filters, name='get_furniture_filters'),
    url(r'^filter/(?P<furniture_type>[a-z]+)/$', filtered_furnitures, name='filtered_furnitures'),
    # url(r'^student', student_detail, name='student-detail'),
    # url(r'^$', HomePageView.as_view(), name='index-view')
]