from django.contrib import admin
from . models import Portfolio,Email,Contact,BlogPost,Second,Tag
from . models import Shop , Tagshop , Indexview , OrderItem ,Order,Brand

# Register your models here.


admin.site.register(Indexview)
admin.site.register(Brand)



class OrderItemTupleInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname','address_1','address_2','post','country','state','Town','address_3','address_4','postcode','country_1','state_1','Town_1')
    inlines = [OrderItemTupleInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title' , 'dec' , 'image')
    

admin.site.register(Email)

@admin.register(Contact)
class ContactfmAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message')
    


    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tagshop)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    


@admin.register(BlogPost)
class BlogPostfmAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','image','publish_date')


@admin.register(Second)
class SecondfmAdmin(admin.ModelAdmin):
    list_display = ('title','image','pub_date')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title','images','dec','image','price','brand')
    
