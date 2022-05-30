from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.ProjectView import ProjectListView,ProjectDetailView

from .views.registration import (
    UserRegistrationView,
    UserLoginView,
    UserListView,
    UserDetailView,
)
from .views.ProductView import (
    ProductViewSet,
    SectorViewSet,
    SubProductsListView,
    ProductDetailView,
    ParentProductsListView,
    ProductPostLikePushView,
    ProductPostLikePopView,
    ProductPostDisLikePushView,
    ProductPostDislikePopView,
    ProductPostLovePushView,
    ProductPostLovePopView,
    ProductNestedView
)

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('users', UserListView.as_view(), name='users'),
    path('user/me', UserDetailView.as_view(), name='user'),
    path('products', ProductViewSet.as_view(), name='products'),
    path('sectors', SectorViewSet.as_view(), name='sectors'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('products/<int:pk>', SubProductsListView.as_view(), name='sub_products'),
    path('parents/<int:pk>', ParentProductsListView.as_view(), name='parents'),
    path('projects/<int:pk>', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
    path('product/like/push/<int:pk>', ProductPostLikePushView.as_view(), name='product_like_push'),
    path('product/like/pop/<int:pk>', ProductPostLikePopView.as_view(), name='product_like_pop'),
    path('product/dislike/push/<int:pk>', ProductPostDisLikePushView.as_view(), name='product_dislike_push'),
    path('product/dislike/pop/<int:pk>', ProductPostDislikePopView.as_view(), name='product_dislike_pop'),
    path('product/love/push/<int:pk>', ProductPostLovePushView.as_view(), name='product_love_push'),
    path('product/love/pop/<int:pk>', ProductPostLovePopView.as_view(), name='product_like_pop'),
    path('products/nested', ProductNestedView.as_view(), name='products_nested_view'),
]