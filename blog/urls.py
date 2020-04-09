from . import views
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('about/', view.AboutView.as_view(), name='about'),
    path('reference/', views.ReferenceView.as_view(), name='reference'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
