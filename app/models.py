from django.db import models
from django.contrib.auth.models import (AbstractUser, UserManager)
from ckeditor.fields import RichTextField


class UserManagerAccounts(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('Users must have a password')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(
        'email address', null=False, blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManagerAccounts()


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='account')
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices, blank=False, null=False)
    profile_image = models.URLField(
        default='https://www.meme-arsenal.com/memes/8b6f5f94a53dbc3c8240347693830120.jpg', null=False, blank=False)
    background_image = models.URLField(
        default="https://wallpapercave.com/wp/wp3589893.jpg", null=False, blank=False)

    def __str__(self):
        return f'{self.user.email} |Profile'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_posts(self):
        return self.user.posts.all()

    def get_friends(self):
        return


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    # content = models.TextField(null=False, blank=False)
    content = RichTextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'{self.content[:20]}... | User: {self.user.account.get_full_name()} | Date: {self.date_posted}'

    def get_comments(self):
        return self.comments.all()

    def get_likes(self):
        return self.likes.all()

    def get_likes_number(self):
        return self.likes.count()

    def get_comments_number(self):
        return self.comments.count()


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content[:20]}... | Post: {self.post.content[:10]} | User: {self.user.account.get_full_name()} | Date: {self.date_commented}'


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post: {self.post.content[:20]}... | User: {self.user.account.get_full_name()}'
