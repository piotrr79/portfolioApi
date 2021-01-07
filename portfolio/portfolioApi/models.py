from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_reference = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'portfolio_category'
                    
class Blog(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    lead = models.CharField(max_length=255)
    content = models.TextField()
    link_url = models.URLField()
    photo = models.ImageField(upload_to='uploads')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        db_table = 'portfolio_blog'
 
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    
    class Meta:
        db_table = 'portfolio_article'
        
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title