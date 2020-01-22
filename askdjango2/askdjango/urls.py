from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', lambda req: redirect('blog:post_list'), name='root'),  #URL reverse
    path('accounts/', include('accounts.urls')),
]
