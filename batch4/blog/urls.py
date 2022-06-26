from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import *


urlpatterns = [


    path("createpost/", CreatePost, name="createpost"),
    path("allposts/", Allpost, name="Allposts"),
    path("allposts/<int:id1>/", SpecificPost, name="sp_post"),
    path("pages/<int:page>/", Allpost, name="pages"),
    path("post/new/", PostCreateView.as_view(),name="cls-post-create"),
    path("post/view/", PostListView.as_view(),name="cls-post-view"),
    path("post/myposts/", UserPostListView.as_view(),name="cls-user-post-view"),
    path("post/<int:pk>/", PostDetailView.as_view(),name="cls-post-sp"),
    path("post/otherpost/<str:u1>/", OtherUserPostListView.as_view(),name="otheruserpost"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(),name="cls-post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(),name="cls-post-delete"),
    path("posts/<int:id1>/", CommentPost,name="post-comment"),
    path("posts/<int:id1>/approve", comment_approve,name="post-approve"),





]