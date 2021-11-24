from django.urls import path
from .views import view_home_page, view_test1, view_test2, view_test3, view_final_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('', view_home_page, name='home'),
    path('test/1', view_test1, name='test1'),
    path('test/2', view_test2, name='test2'),
    path('test/3', view_test3, name='test3'),
    path('final/', view_final_page, name='final'),
    # path('<int:pk>/create/massage', SendMessageCreateView.as_view(), name='create_message'),
    # path('show/product/<slug:pk>', ShowProduct.as_view(), name='show_product')
]

urlpatterns += staticfiles_urlpatterns()