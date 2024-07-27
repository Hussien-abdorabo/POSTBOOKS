from django.urls import path
from . import views


urlpatterns = [
   path("blog/",views.index, name="blog-index"),   
   path("post-detail/<int:id>/",views.post_detail, name="blog-post-detail"),   
   path("post-edit/<int:id>/",views.post_edit, name="blog-post-edit"),   
   path("post-delete/<int:id>/",views.post_delete, name="blog-post-delete"),   
]
