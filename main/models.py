from django.db import models

EXER_TYPE = (
    ('stretch', 'STRETCH'),
    ('exercise', 'Exercise')
)

class Category(models.Model):
    label = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.label

class Tag(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Exer(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    image_1 = models.ImageField(upload_to="exers", null=True, blank=True)
    image_2 = models.ImageField(upload_to="exers", null=True, blank=True)
    image_3 = models.ImageField(upload_to="exers", null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Workout(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    exers = models.ManyToManyField(Exer)

    def __str__(self):
        return self.title