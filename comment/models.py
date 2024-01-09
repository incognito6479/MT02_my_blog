from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.PROTECT)
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        