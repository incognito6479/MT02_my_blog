from django.db import models


class Post(models.Model):
    STATUS = (
        ('available', 'Available'),
        ('archived', 'Archived'),
    )

    author = models.ForeignKey('user.User', on_delete=models.PROTECT) # cascade protect set_default set_null set do_nothing
    title = models.CharField(max_length=256)
    body = models.TextField()
    num_of_views = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        