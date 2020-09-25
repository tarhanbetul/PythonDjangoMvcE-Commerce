from django.urls import path

from . import views

app_name = 'home' #uygulamanın adını path ile çağırmak için

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('contact', views.contact_form, name='contact'),
    path('kategoriler', views.show_category),
    path('login', views.login_form),
    path('join', views.join_form),
    path('logout', views.login_out),
    path('category/<int:catid>',views.category),
    path('product/<int:proid>',views.product),



]
