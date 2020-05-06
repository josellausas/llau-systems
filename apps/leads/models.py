from django.db import models


class EmailLead(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=1024, default="main")
    
    def __str__(self):
        return f"{topic}:{email}"

    class Meta:
        ordering = ['-created']