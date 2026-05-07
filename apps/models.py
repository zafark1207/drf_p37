from django.contrib.auth.models import AbstractUser
from django.db.models import Model, BooleanField, ForeignKey, CASCADE, DecimalField, DateTimeField, ImageField, \
    OneToOneField, ManyToManyField, Manager, FloatField

from django.db.models import CharField, TextField, IntegerField, PositiveIntegerField


# class Post(Model):
#     userId = IntegerField(db_default=0)
#     title = CharField(max_length=255)
#     body = TextField()


# class Comment(Model):
#     postId = ForeignKey('apps.Post', on_delete=CASCADE)
#     name = CharField(max_length=255)
#     email = CharField(max_length=255)
#     body = TextField()


# class Album(Model):
#     userId = IntegerField(db_default=0)
#     title = CharField(max_length=255)
#
#
# class Photo(Model):
#     albumId = ForeignKey('apps.Album', on_delete=CASCADE)
#     title = CharField(max_length=255)
#     url = CharField(max_length=255)
#     thumbnailUrl = CharField(max_length=255)
#
#
# class Book(Model):
#     title = CharField(max_length=255)
#     author = CharField(max_length=255)
#     price = DecimalField(max_digits=10, decimal_places=2)
#     published_year = IntegerField()
#     is_available = BooleanField(default=True)
#
#
# class Student(Model):
#     class GradeTextChoice(TextChoices):
#         A = 'a', 'A'
#         B = 'b', 'B'
#         C = 'c', 'C'
#
#     name = CharField(max_length=255)
#     age = IntegerField()
#     grade = CharField(max_length=2, choices=GradeTextChoice.choices, default=GradeTextChoice.A)
#     is_active = BooleanField(default=True)
#     image = ImageField(upload_to='images/', blank=True, null=True)
#     created_at = DateTimeField(auto_now_add=True)


# Product

# djangorestframework-simplejwt
# class Product(Model):
#     name = CharField(max_length=255)
#     price = DecimalField(max_digits=10, decimal_places=2)
#     userid = ForeignKey('apps.User', on_delete=CASCADE, related_name='products')


# class Post(Model):
#     title = CharField(max_length=255)
#     content = TextField()
#     author = ForeignKey('apps.User', CASCADE, related_name='posts')
#     created_at = DateTimeField(auto_now_add=True)
#     is_published = BooleanField(default=False)


#     category = ForeignKey('apps.Category', CASCADE, related_name='posts')
#     tags = ManyToManyField('apps.Tag', related_name='posts')
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#
#
# class Tag(Model):
#     name = CharField(max_length=255)
#
#
# #
# # class ProductTag(Model):
# #     product = ForeignKey('apps.Product', CASCADE, related_name='tags')
# #     tag = ForeignKey('apps.Tag', CASCADE, related_name='products')
#
#
# class Like(Model):
#     user = ForeignKey('apps.User', CASCADE, related_name='likes')
#     post = ForeignKey('apps.Post', CASCADE, related_name='likes')
#
#     unique_together = (
#         ('user', 'post'),
#     )

class User(AbstractUser):
    phone = CharField(max_length=15, null=True, blank=True)


# class Category(Model):
#     name = CharField(max_length=255)
#
#
# class Product(Model):
#     title = CharField(max_length=255)
#     description = TextField()
#     price = DecimalField(max_digits=10, decimal_places=2)
#     category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
#     is_active = BooleanField(default=True)
#     created_at = DateTimeField(auto_now_add=True)
#
#
# class Favorite(Model):
#     user = ForeignKey('apps.User', on_delete=CASCADE, related_name='favorites')
#     product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='favorites')
#
#     unique_together = (
#         ('user', 'product'),
#     )
#
#
# from django.db.models import F
#
#
# class BookManager(Manager):
#     def annotate_with_availability(self):
#         return self.get_queryset().annotate(
#             available_count=F('total_copies') - F('borrowed_copies')
#         )
#
#
# class Book(Model):
#     title = CharField(max_length=255)
#     author = CharField(max_length=255)
#     year_published = PositiveIntegerField()
#     rating = FloatField(default=0.0)
#     total_copies = PositiveIntegerField()
#     borrowed_copies = PositiveIntegerField()
#
#     objects = BookManager()
#
#     def __str__(self):
#         return self.title


class Category(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(Model):
    title = CharField(max_length=255)
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='posts')
    content = TextField()
    author = ForeignKey('apps.User', CASCADE, related_name='posts')
    created_at = DateTimeField(auto_now_add=True)
    views_count = IntegerField(default=0)
    tags = ManyToManyField('apps.Tag', related_name='posts', blank=True)


class PostTag(Model):
    post = ForeignKey('apps.Post', CASCADE, related_name='post_tags')
    tag = ForeignKey('apps.Tag', CASCADE, related_name='tag_post')


class Like(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='likes')
    post = ForeignKey('apps.Post', on_delete=CASCADE, related_name='likes')

    unique_together = (
        ('user', 'post'),
    )
