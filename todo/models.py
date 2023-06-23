from django.db import models



#title , text, creat ,date, status, about, user


class TODO(models.Model):
    STATUS=(
        ("H","HIGH"),
        ("M", "MEDIUM"),
        ("L","LOW"),
    )
    
    
    title=models.CharField(max_length=150)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=10)
    def __str__(self):
        return self.title