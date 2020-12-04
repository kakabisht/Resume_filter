from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    github=models.URLField(max_length=254,blank=True)
    linkedin=models.URLField(max_length=254,blank=True)
    portfolio_site=models.URLField(max_length=254,blank=True)
    resume=models.FileField(upload_to='users/%Y/%m/%d/', blank=True)
    voice=models.FileField(upload_to='users/%Y/%m/%d/', blank=True)
    message = models.TextField(max_length=254)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        unique_together = ["user", "message"]
