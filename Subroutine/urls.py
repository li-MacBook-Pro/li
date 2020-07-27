from django.urls import path, re_path

from . import views


urlpatterns = [
    path('HTML_PB/', views.HTML_pb),
    #  /Subroutine/HTML_PB/

    path("views/name/", views.func_v0, name='v0'),
    path("views/v1/", views.func_v1, name='v1'),

    path("form0/<str:name>/", views.func),#form表单  <默认为str:name>可以设置为int等匹配符
    path("views/<name>/", views.func),

    re_path("^9\d{4}/$", views.re),

    path('temp/', views.templstes_0),
    path('demo01/<username>/', views.templstes_1),

    path('json/', views._json),
]
#  /Subroutine/HTML_PB/    /Subroutine/views/name/    /Subroutine/views/v1/
#  /Subroutine/views/li/
#   /Subroutine/temp/       /Subroutine/demo01/<username>/    /Subroutine/json/