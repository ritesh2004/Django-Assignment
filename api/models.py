from django.db import models

# Create your models here.

class TelegramUsers(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"TelegramUser(id={self.id}, username={self.username})"