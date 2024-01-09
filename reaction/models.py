from django.db import models

class Reaction(models.Model):
    REACTION = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    post = models.ForeignKey('post.Post', on_delete=models.PROTECT)
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    reaction = models.CharField(choices=REACTION)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.reaction}"

    class Meta:
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'
        