from sys import path

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from apps.views import PostCommentListAPIView, \
#     PostRetrieveUpdateDestroyAPIView, AlbumRetrieveUpdateDestroyAPIView, \
#     AlbumPhotoListAPIView, UserListAPIView, PhotoRetrieveUpdateDestroyAPIView, CommentRetrieveUpdateDestroyAPIView, \
#     PostListCreateAPIView, CommentListCreateAPIView, AlbumListCreateAPIView, PhotoListCreateAPIView, BookListCreateAPIView, BookDetailAPIView, StudentListCreateAPIView



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()
router.register('posts', PostModelViewSet,)


urlpatterns = [
    path('', include(router.urls)),
    # path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view()),
    #path('posts', PostListCreteAPIView.as_view()),
    # path('posts/<int:pk>/comments', PostCommentListAPIView.as_view()),
    # path('comments', CommentListCreateAPIView.as_view()),
    # path('comments/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),
    #path('users', UserListAPIView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/<int:pk>/todos', UserTodoListAPIView.as_view()),
    # path('users/<int:pk>/albums', UserAlbumListAPIView.as_view()),
    # path('users/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('albums', AlbumListCreateAPIView.as_view()),
    # path('photos', PhotoListCreateAPIView.as_view()),
    # path('photos/<int:pk>', PhotoRetrieveUpdateDestroyAPIView.as_view()),
    # path('todos', TodoListCreateAPIView.as_view()),
    # path('todos/<int:pk>', TodoRetrieveUpdateDestroyAPIView.as_view()),
    # path('albums/<int:pk>', AlbumRetrieveUpdateDestroyAPIView.as_view()),
    # path('albums/<int:pk>/photos', AlbumPhotoListAPIView.as_view()),
    # path('books', BookListCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('students', StudentListCreateAPIView.as_view()),
    # path('posts', PostListCreteAPIView.as_view()),
    # path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view()),
    #path('books', BookListCreateAPIView.as_view()),

]
