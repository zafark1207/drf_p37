from django.core.serializers import get_serializer
from django.db.migrations import serializer
from django.db.models import Model, Count, Q, Exists, OuterRef, Value, F
from django.db.models.fields import BooleanField
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

import manage
from apps.filters import PostFilter
from apps.models import User, Post, Like
from apps.permissions import IsAuthor, CustomPostPermission
# from apps.permissions import IsAuthor
from apps.serializers import UserModelSerializer, PostModelSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, \
    RetrieveAPIView


# @extend_schema(tags=['posts'])
# class PostListAPIView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostModelSerializer


# @extend_schema(tags=['comments'])
# class CommentListCreateAPIView(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentModelSerializer
#
#
# @extend_schema(tags=['albums'])
# class AlbumListCreateAPIView(ListCreateAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumModelSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('userId',)
#
#
# @extend_schema(tags=['albums'])
# class AlbumRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumModelSerializer
#
#
# @extend_schema(tags=['albums'])
# class AlbumPhotoListAPIView(ListAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get('pk')
#         return qs.filter(albumId=pk)
#
#
# @extend_schema(tags=['photos'])
# class PhotoListCreateAPIView(ListCreateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoModelSerializer
#
#
# @extend_schema(tags=['photos'])
# class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoModelSerializer
#
#
# @extend_schema(tags=['users'])
# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#     permission_classes = [IsAuthenticated]
#
#
# @extend_schema(tags=['posts'])
# class PostListCreateAPIView(ListCreateAPIView):
#     queryset = Post.objects.order_by('-id')
#     serializer_class = PostModelSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('userId',)
#
#
# @extend_schema(tags=['posts'])
# class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostModelSerializer
#
#
# @extend_schema(tags=['posts'])
# class PostCommentListAPIView(ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         pk = self.kwargs.get('pk')
#         return qs.filter(postId=pk)
#
#
# @extend_schema(tags=['comments'])
# class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.order_by('-id')
#     serializer_class = CommentModelSerializer
#
#
# @extend_schema(tags=['books'])
# class BookListCreateAPIView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# @extend_schema(tags=['books'])
# class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#
# @extend_schema(tags=['students'])
# class StudentListCreateAPIView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     # filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
#     # search_fields = ('name',)
#     # filterset_class = StudentFilter
#     # ordering_fields = ('age', 'created_at')


# @extend_schema(tags=['users'])
# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#
# class DownloadAPIView(GenericAPIView):
#     permission_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request):
#         serializer = self.serializer_class(self.queryset, many=True).data
#         return FileResponse(serializer, as_attachment=True, filename='posts.json')
#
#
# # @extend_schema(tags=['posts'])
# class PostListCreteAPIView(ListCreateAPIView):
#     queryset = Post.objects.order_by('-created_at')
#     serializer_class = PostSerializer
#     permission_classes = []
#
#     filter_backends = [DjangoFilterBackend, SearchFilter, ]
#     filterset_class = PostFilter
#     search_fields = ['title', 'content']

# def get_queryset(self):
#     qs = super().get_queryset()
#     return qs.annotate(likes_count=Count('likes'))


#
#
# class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated, IsAuthor]
#

# class ProductModelViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         user = self.request.user
#
#         if user.is_authenticated:
#             key = Exists(Favorite.objects.filter(product_id=OuterRef('pk'), user=user))
#         else:
#             key = Value(False, BooleanField())
#
#         return qs.annotate(favorites_count=Count('favorites'),
#                            is_favorited=key
#                            )


# class BookListCreateAPIView(ListCreateAPIView):
#     queryset = Book.objects.annotate_with_availability()
#     serializer_class = BookSerializer
#     filterset_class = BookFilter
#
#     filter_backends = [SearchFilter, OrderingFilter]
#
#     ordering_fields = ['rating', 'year_published']
#
#     ordering = ['-rating', 'year_published']
#
#
# class RegisterAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [CustomPostPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'likes__count']
    ordering = ['-created_at', 'views_count']

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            key = Exists(Like.objects.filter(product_id=OuterRef('pk'), user=user))
        else:
            key = Value(False, BooleanField())

        return qs.annotate(likes_count=Count('likes'),
                           is_liked=key)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save(update_fields=['views_count'])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='my-posts')
    def my_posts(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Ushbu sahifani ko'rish uchun avval tizimga kiring."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        user_posts = self.get_queryset().filter(author=request.user)

        # Agar pagination sozlangan bo'lsa, uni ham inobatga olamiz
        page = self.paginate_queryset(user_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='like')
    def toggle_like(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Like bosish uchun tizimga kirishingiz shart."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        post = self.get_object()
        user = request.user

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            status_msg = "unliked"
            status_code = status.HTTP_200_OK
        else:
            post.likes.add(user)
            status_msg = "liked"
            status_code = status.HTTP_201_CREATED

        return Response(
            {
                "status": status_msg,
                "total_likes": post.likes.count()
            },
            status=status_code
        )
