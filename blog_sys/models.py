from django.db import models
# superuser:hhh password:hhh111222


# Create your models here.
class Theme(models.Model):
    theme_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'theme'

    def __unicode__(self):
        return self.theme_name


class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_read_number = models.PositiveIntegerField()
    blog_publish_time = models.DateField(auto_now=True)
    blog_theme = models.ForeignKey("Theme", on_delete=models.SET_DEFAULT, default=1)
    # if the theme is delete,blog will not delete, and change theme to 1,it means no theme
    blog_author = models.ForeignKey("Author", on_delete=models.CASCADE)
    # support null

    class Meta:
        db_table = 'blog'

    def __unicode__(self):
        return self.blog_name


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_password = models.CharField(max_length=100)
    author_email = models.EmailField()
#     I could add session in Author to save session state

    class Meta:
        db_table = 'author'

    def __unicode__(self):
        return self.author_name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    comment_blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    comment_user = models.ForeignKey("Author", on_delete=models.CASCADE)
    reply = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    # reply is not complete,I think next should make a single class to finish reply
    # could have reply user,reply time and so on.and have a list reply

    class Meta:
        db_table = 'comment'

    def __unicode__(self):
        return self.content


