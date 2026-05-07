from datetime import datetime

from django.contrib.admin import action
from django.db.models import Count
from django.template.context_processors import request
from django.utils.timezone import now
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, BooleanField, DateTimeField, HiddenField, CurrentUserDefault, \
    ImageField, IntegerField, CharField, ListField
from rest_framework.permissions import IsAuthenticated
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apps.models import User

# class PostModelSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#
# class CommentModelSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# class AlbumModelSerializer(ModelSerializer):
#     class Meta:
#         model = Album
#         fields = '__all__'
#
#
# class PhotoModelSerializer(ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = '__all__'
#
#
# class BookModelSerializer(ModelSerializer):
#     is_expensive = SerializerMethodField()
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#     def get_is_expensive(self, obj):
#         return obj.price > 100
#
#     def validate_price(self, value):
#         if value < 0:
#             raise ValidationError('Narx 0 dan kichik bo`lmasligi kerak')
#         return value
#
#     def validate_published_year(self, value):
#         if value < 1900 or value > now().year:
#             raise ValidationError(f'Yil 1900 dan {now().year} gacha bo`lishi kerak')
#         return value
#
#
# class StudentModelSerializer(ModelSerializer):
#     is_adult = SerializerMethodField()
#
#     # address = SerializerMethodField()
#     # faolmi = BooleanField(source='is_active', read_only=True)
#
#     class Meta:
#         model = Student
#         fields = '__all__'
#         # exclude = ('is_active',)
#
#     # def get_address(self, obj: Student):
#     #     if obj.id % 2 == 0:
#     #         return 'Toshkent'
#     #     return None
#
#     def get_is_adult(self, obj: Student):
#         return obj.age >= 18
#
#     def validate_age(self, value):
#         if value < 5:
#             raise ValidationError('Yosh 5 dan kichik bo`lmasligi kerak')
#         return value
#
#     def validate_grade(self, value: str):
#         if value.upper() not in ['A', 'B', 'C']:
#             raise ValidationError('Daraja faqat A, B, C bo`lishi mumkin')
#         return value
#
#     def validate_name(self, value: str):
#         if not value.lower().replace("g'", '').replace("o'", '').isalpha():
#             raise ValidationError('Ism emasku bu!')
#         return value
#
#     def to_representation(self, instance: Student):
#         repr = super().to_representation(instance)
#         if instance.id % 2 == 0:
#             repr['address'] = 'Toshkent'
#         return repr


# class PostSerializer(ModelSerializer):
#     created_at = DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
#     author = HiddenField(default=CurrentUserDefault())
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#     def is_liked(self, obj):
#         return obj.likes.filter(id=self.context['request'].user.id).exists()


# class ProductModelSerializer(ModelSerializer):
#     favorites_count = SerializerMethodField()
#     is_favorited = SerializerMethodField()
#
#     class Meta:
#         model = Product
#         excluded = ('category',)
#         read_only_fields = ('category',)
#
#     def get_favorites_count(self, obj: Product):
#         return obj.favorites_count
#
#     def get_is_favorited(self, obj: Product):
#         return obj.is_favorited
#
#
# @action(detail=False, methods=['get'], url_path='products', permission_classes=[IsAuthenticated],
#         serializer_class=ProductModelSerializer)
# def products(self, request):
#     user = request.user
#     qs = self.get_queryset().filter


from datetime import date


# class BookSerializer(ModelSerializer):
#     is_classic = SerializerMethodField()
#     available_count = IntegerField(read_only=True)
#
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'year_published', 'rating', 'available_count', 'is_classic',
#                   'total_copies', 'borrowed_copies', ]
#
#     def get_is_classic(self, obj):
#         current_year = date.today().year
#         return (current_year - obj.year_published) > 10
#
#
# class RegisterModelSerializer(ModelSerializer):
#     first_name = CharField(max_length=150, write_only=True)
#     password = CharField(write_only=True)
#     confirm_password = CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'phone')
#
#     def validate(self, data):
#         if data.pop('confirm_password') != data.get('password'):
#             raise ValidationError('Passwords do not match')
#         return data
#
#     def validate_phone(self, value):
#         if value.startswith('+998'):
#             if value.isdigit() and len(value) == 13:
#                 return value
#             raise ValidationError('Phone number must be 13 digits long and start with +998')
#         else:
#             raise ValidationError('Phone number must start with +998')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


from rest_framework import serializers
from apps.models import Post, Tag

from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )
    tag_names = serializers.SlugRelatedField(
        source='tags',
        many=True,
        read_only=True,
        slug_field='name'
    )
    likes_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.BooleanField(read_only=True)

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'category', 'content', 'created_at',
            'author', 'views_count', 'tags', 'tag_names',
            'likes_count', 'is_liked'
        ]
        read_only_fields = ['author', 'views_count']

    def _get_or_create_tags(self, tags_data):
        tag_objects = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip().lower())
            tag_objects.append(tag)
        return tag_objects

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(self._get_or_create_tags(tags_data))
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        instance = super().update(instance, validated_data)
        if tags_data is not None:
            instance.tags.set(self._get_or_create_tags(tags_data))
        return instance
