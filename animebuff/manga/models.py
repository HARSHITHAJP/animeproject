from django.db import models
from django.contrib.auth.models import User



class genretbl(models.Model):
    genre = models.CharField(max_length=30, verbose_name="Genre")

    def __str__(self):
        return self.genre

class booktbl(models.Model):
    book_isbn =  models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=40, verbose_name="Title")
    genre = models.ForeignKey(genretbl ,null=True, blank=True, on_delete=models.CASCADE,)
    author= models.CharField(max_length=30,verbose_name="Author")
    description = models.CharField(max_length=100, verbose_name="Description")
    posted_date_time = models.DateTimeField( auto_now_add=True, verbose_name="posted on")
    posted_by = models.ForeignKey(User ,null=True, blank=True, on_delete=models.CASCADE,)
    book_pic=models.ImageField(null=True, blank=True,default='default.jpg',upload_to='static/uploadimg/', verbose_name="Photo")
    book=models.FileField(null=True, blank=True,default='default.jpg',upload_to='static/pdfs/', verbose_name="PDF")
    

    def __str__(self):
        return self.posted_by


    
class volumetbl(models.Model):
    volume_no = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=200, verbose_name="Description")
    book_isbn = models.ForeignKey(booktbl ,null=False, on_delete=models.CASCADE,)
    genre = models.ForeignKey(genretbl ,null=True, blank=True, on_delete=models.CASCADE,)


