from django.db import models


class User(models.Model):
    username = models.CharField(max_length=36, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)  # Store hashed passwords
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    tg = models.URLField(blank=True, null=True)  # Telegram link
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Topic(models.Model):
    name_topic = models.CharField(max_length=28, unique=True)

    def __str__(self):
        return self.name_topic


class City(models.Model):
    name_city = models.CharField(max_length=28, unique=True)

    def __str__(self):
        return self.name_city


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Cities ")
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name="Topics")
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title


