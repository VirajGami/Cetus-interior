from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from .import views  
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
     path('subscribe/', views.subscribe, name='subscribe'),
    path('myrequirement/', views.myrequirement, name='myrequirement'),
    path('register/', views.register, name='register'),
    path('brochurelist/', views.brochurelist, name='brochurelist'),
    path('images/', views.images, name='images'),
    path('loggedIn',views.cust_login1,name="cust_login1"),
    path('product/', views.product, name='product'),
    path('loggedOut', views.logout, name="logout"),
    path('deleterequirement/<int:id>', views.deleterequirement, name='deleterequirement'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('sendrequirnment/', views.sendrequirnment, name='sendrequirnment'),
    path('registersubmit/', views.registersubmit, name='registersubmit'),  
    path('requirnmentsubmit/', views.requirnmentsubmit, name='requirnmentsubmit'),
    path('productBycategory/<int:id>', views.productbycategory, name='productbycategory'),
    path('contactsubmit/', views.contactsubmit, name='contactsubmit'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)