from django.db import models
from slugify import slugify



class CarouselImage(models.Model):
    image = models.ImageField(upload_to="images/")

class Category(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="photos")
    text = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} -> {self.text}"

    class Meta:
        ordering = ('-created_at',)


class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.TextField(max_length=60)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ('-created_at',)
