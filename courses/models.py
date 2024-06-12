from django.db import models
from django.utils.html import escape

class Course(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default='Anthony Violet')
    thumbnail = models.ImageField(upload_to='static/uploads/thumbnails/courses/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lecons')
    name = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()

    def clean(self):
        # Remplacer les chevrons <?php et ?> par leurs équivalents HTML
        if self.content:
            self.content = self.content.replace('<?php', '&lt;?php')
            self.content = self.content.replace('?>', '?&gt;')

    def __str__(self):
        return self.name