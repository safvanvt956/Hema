from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# ============= Index ============== #

class Indexview(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    images = models.ImageField()
    oldprice = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address_1=models.TextField()
    address_2=models.TextField(max_length=100)
    post=models.IntegerField()
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    Town=models.CharField(max_length=50)
    address_3=models.TextField()
    address_4=models.TextField(max_length=100)
    postcode=models.IntegerField()
    country_1=models.CharField(max_length=100)
    state_1=models.CharField(max_length=50)
    Town_1=models.CharField(max_length=50)
    

    def __str__(self):
        return self.firstname
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/order_image')
    quantity=models.IntegerField()
    price=models.IntegerField()
    total=models.IntegerField()
    

# ============ Filter =============== #


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    dec = models.CharField(max_length=100)
    image= models.ImageField()

    fashion = models.BooleanField(default=False)
    shoes = models.BooleanField(default=False)
    electronic = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
    
    
# ============ Contact =============== #
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    

    

# ============== Email =============== #
    

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
        

# =============== Blog =============== #

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField()
    publish_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)


# Category boolean count

    fashion = models.BooleanField(default=False)
    beauty = models.BooleanField(default=False)
    accessories = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    life_style = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    

class Second(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


   
# ============= Search shop results etc ============== #


class Tagshop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    image = models.ImageField()
    images = models.ImageField()
    dec = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    tag = models.ManyToManyField(Tagshop)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)

    shirt = models.BooleanField(default=False)
    jean = models.BooleanField(default=False)
    woman = models.BooleanField(default=False)
    ring = models.BooleanField(default=False)
    bag = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    shoe = models.BooleanField(default=False)
    elect = models.BooleanField(default=False)
    cosm = models.BooleanField(default=False)

    color = models.CharField(max_length=20, choices=[
        ('white', 'White'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('orange', 'Orange'),
    ])

    size = models.CharField(max_length=10, choices=[
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('25', 'Size 25'),
        ('35', 'Size 35'),
        ('40', 'Size 40'),
    ], blank=True, null=True)


    def __str__(self):
        return self.title

    
    
    
