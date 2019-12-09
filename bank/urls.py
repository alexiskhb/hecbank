from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from bank.views import make_payment


urlpatterns = [
    # url(r"^admin/", admin.site.urls),
    # url(r'^login/$', auth_views.login, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    url(r'^payment_ok/$', TemplateView.as_view(template_name='payment_ok.html'), name='payment_ok'),
    url(r'^payment_error/$', TemplateView.as_view(template_name='payment_error.html'), name='payment_error'),
    url(r'^make_payment/$', make_payment, name='make_payment'),
    url(r'^$', TemplateView.as_view(template_name='game_results.html'), name='index'),
]
