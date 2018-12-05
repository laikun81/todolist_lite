from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.CharField(
        max_length=100,
        verbose_name="TASK",        
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="INS_DATETIME"
    )