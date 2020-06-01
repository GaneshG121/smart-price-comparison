from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class ScraperItem(models.Model):
    time = models.CharField(max_length=32)
    date = models.CharField(max_length=100)
    image = models.CharField(max_length=624)
    link1 = models.CharField(max_length=624)
    days1 = models.CharField(max_length=32)
    price1 = models.CharField(max_length=20)
    link2 = models.CharField(max_length=624)
    days2 = models.CharField(max_length=32)
    price2 = models.CharField(max_length=32)
    link3 = models.CharField(max_length=624)
    days3 = models.CharField(max_length=32)
    price3 = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=6122)
    location = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.title


'''class Classifications(models.Model):
    time = models.CharField(max_length=32)
    date = models.CharField(max_length=100)
    image = models.CharField(max_length=644)
    link1 = models.CharField(max_length=624)
    price1 = models.CharField(max_length=20)
    link2 = models.CharField(max_length=624)
    price2 = models.CharField(max_length=32)
    link3 = models.CharField(max_length=624)
    price3 = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    ram = models.CharField(max_length=644)
    storage = models.CharField(max_length=624)
    #dispaly = models.CharField(max_length=20)
    os = models.CharField(max_length=644)
    color = models.CharField(max_length=624)
    camera = models.CharField(max_length=20)
    sim = models.CharField(max_length=624)
    network = models.CharField(max_length=32)
   # warrenty = models.CharField(max_length=624)
    battery = models.CharField(max_length=32)
    description = models.CharField(max_length=61122)
    location = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    def publish(self):
        self.time = timezone.now()
        self.save()'''

    # date=scrapy.Field()
    # time=scrapy.Field()
    # image=scrapy.Field()
    # link=scrapy.Field()
    # title=scrapy.Field()
    # description=scrapy.Field()
    # location=scrapy.Field()
    # price=scrapy.Field()
    # category=scrapy.Field()
