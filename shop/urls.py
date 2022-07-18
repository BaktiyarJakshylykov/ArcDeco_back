from .views import ShopView, ProductDetailView, ContactView, MessageView, FilterNameView, PartnerView, ReviewView, \
    calculator, CategoryView
from django.urls import path


urlpatterns = [
    path('home/', CategoryView.as_view(), name='home'),
    path('home_list', ShopView.as_view(), name='home_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('message/', MessageView.as_view(), name='message'),
    path('title-search/<str:title>/', FilterNameView.as_view(), name='titlesearch'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('review/', ReviewView.as_view(), name='review'),
    path('addmovie/', calculator, name='addmovie')
    # path('register', RegisterView.as_view(), name='register')
]
#
