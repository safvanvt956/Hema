from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [


    path('',views.index,name='index'),
    path('about/',views.aboutus_style1,name='aboutus-style1'),
    path('blog_grid/',views.blog_grid,name='blog-grid-sidebar'),
    path('blog-details/<int:id>/',views.blog_details,name='blog-details'),
    path('success/',views.success,name='order-success'),
    path('contact/',views.contact,name='contact-style1'),
    path('error-404/',views.error_404,name='error-404'),
    path('login/',views.login1,name='login'),
    path('my-account/',views.my_account,name='my-account'),
    path('portfolio/',views.portfolio_page,name='portfolio-page'),
    path('register/',views.register,name='register'),
    path('search_results/',views.shop_search_results,name='shop-search-results'),
    path('checkout/',views.checkout,name='checkout-style1'),
    path('like/',views.like,name='wishlist-style1'),
    path('layout/',views.loyout,name='product-layout1'),
    path('product/',views.product_variable,name='product-variable'),

    path('logout/',views.logout,name='logout'),

    # path('cart/',views.cart,name='cart-style1'),

    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart'),
    
    
    # path('forgot-password/',views.forgot_password,name='forgot-password'),

    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]