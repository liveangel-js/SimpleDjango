from django.db import models
from django.contrib import admin
# Create your models here.

class BlogPost(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


class Meta:
    order = ('-timestamp',)

class Archive(models.Model):
    bookid = models.AutoField(primary_key=True)
    booklist = models.ForeignKey(BlogPost)

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('bookid',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Archive, ArchiveAdmin)