from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return f'{self.user.username} and {self.friend.username}'
    

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')

    def __str__(self):
        return f'{self.from_user.username} to {self.to_user.username}'