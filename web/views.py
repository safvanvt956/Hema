from django.shortcuts import render,redirect, get_object_or_404
from . models import Portfolio,BlogPost,Second,Brand
from . models import Shop , Indexview ,Order,OrderItem
from .forms import ContactForm, Emailform
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cart.cart import Cart





# Create your views here.


def index(request):

    shop = Indexview.objects.all()

    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('index')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form,
        'productview' : shop,
        }

    return render(request,'index.html',context)



@login_required(login_url="login")
def cart_add(request, product_id):
    cart = Cart(request)
    product = Indexview.objects.get(id=product_id) 
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Indexview.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Indexview.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Indexview.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('cart')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }
    return render(request, 'cart/cart.html',context)





def aboutus_style1(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('aboutus-style1')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }

    return render(request,'aboutus-style1.html',context)







def blog_grid(request):

    # ============== Email footer ============= #

    email_form = Emailform()  

    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('blog-grid-sidebar')  

    query = request.GET.get('query')
    blog_posts = BlogPost.objects.all()
    recent_posts = Second.objects.all()

    # =============== Search ================ #
    
    if query:
        blog_posts = blog_posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
        recent_posts = Second.objects.filter(title__icontains=query) 

    # =============== Boolean count =========== #

    fashion_count = blog_posts.filter(fashion=True).count()
    beauty_count = blog_posts.filter(beauty=True).count()
    accessories_count = blog_posts.filter(accessories=True).count()
    trending_count = blog_posts.filter(trending=True).count()
    life_count = blog_posts.filter(life_style=True).count()

    all_count = fashion_count + beauty_count + accessories_count + trending_count + life_count  # Total all category

    
    selected_category = request.GET.get("filter" , "*")  #  Category
    
    tag_category = request.GET.get("tag") # Tag

    if tag_category:
        blog_posts = blog_posts.filter(tags__name=tag_category)  

    # =================== Category =================== # 

    # if selected_category != '*':
    #     blog_posts = blog_posts.filter(**{selected_category: True})

    # ================ ☝️ OR Same Category 👇 ================ #

    if selected_category:
        if selected_category == 'fashion':
            blog_posts = blog_posts.filter(fashion=True)
        elif selected_category == 'beauty':
            blog_posts = blog_posts.filter(beauty=True)
        elif selected_category == 'accessories':
            blog_posts = blog_posts.filter(accessories=True)
        elif selected_category == 'trending':
            blog_posts = blog_posts.filter(trending=True)
        elif selected_category == 'life_style':
            blog_posts = blog_posts.filter(life_style=True)


    context = {
        'selected_category': selected_category,
        'tag_category' : tag_category,
        'email_form': email_form,
        'blog_items': blog_posts,
        'blog': recent_posts,
        'all_count': all_count,
        'fashion_count': fashion_count,
        'beauty_count': beauty_count,
        'accessories_count': accessories_count,
        'trending_count': trending_count,
        'life_count': life_count,
        
    }

    return render(request, 'blog-grid-sidebar.html', context)








def blog_details(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('blog-details', id=id)  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form,
        'blog_item': blog_post,
        }
    return render(request,'blog-details.html',context)



def success(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()

            
            uid=request.session.get('_auth_user_id')
            user=User.objects.get(id=uid)
            cart=request.session.get('cart')

            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            post = request.POST.get('postcode')
            country = request.POST.get('address_country1')
            state = request.POST.get('address_State')
            Town = request.POST.get('address_province')
            address_3 = request.POST.get('address_11')
            address_4 = request.POST.get('address_12')
            postcode = request.POST.get('postcode2')
            country_1 = request.POST.get('addresscountry1')
            state_1 = request.POST.get('addressState')
            Town_1 = request.POST.get('addressprovince')


            order = Order(
                user=user,
                firstname=firstname,
                lastname=lastname,
                address_1=address_1,
                address_2=address_2,
                post = post,
                country=country,
                state = state,
                Town=Town,
                address_3=address_3,
                address_4=address_4,
                postcode = postcode,
                country_1=country_1,
                state_1 = state_1,
                Town_1 = Town_1
            )
            order.save()

            for product_id, cart_item in cart.items():
                a = float(cart_item['price'])
                b = int(cart_item['quantity'])
                total = a * b

                order_item = OrderItem(
                    order=order,
                    product=cart_item['name'],
                    image=cart_item['image'],
                    price=a,
                    quantity=cart_item['quantity'],
                    total=total
                )
                order_item.save()

            context = {
                'email_form': email_form
            }
            return render(request, 'order-success.html', context)
        # Handle form validation errors here
    else:
        email_form = Emailform()

    return render(request, 'order-success.html', {'email_form': email_form})






def contact(request):
    contact_form = ContactForm()
    email_form = Emailform()

    if request.method == "POST":
        if "contact" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect("contact-style1")  

        elif "foot" in request.POST:
            email_form = Emailform(request.POST)
            if email_form.is_valid():
                email_form.save()
                return redirect("contact-style1")

    context = {
        "contact_form": contact_form,
        "email_form": email_form
    }
    return render(request, 'contact-style1.html', context)





def error_404(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('error-404')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }
    return render(request,'error-404.html', context)





# def forgot_password(request):
#     if request.method == 'POST':
#         email_form = Emailform(request.POST)
#         if email_form.is_valid():
#             email_form.save()
#             return redirect('index')  
#     else:
#         email_form = Emailform()

#     context = {
#         'email_form': email_form
#         }
#     return render(request,'forgot_password.html' ,context)






def logout(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('index')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }
    return render(request,'login.html',context)



def login1(request):
    email_form = Emailform() # Email footer
    if request.method=="POST": # login
        usname=request.POST.get('customeremail')
        password=request.POST.get('customerpassword')

        email_form = Emailform(request.POST) # footer Email
        if email_form.is_valid():
            email_form.save()
            return redirect('index')

        user = authenticate(username=usname,password=password) # login
        if user is not None:
            login(request,user)
            return redirect('index')

    context = {
        'email_form': email_form
        }
    return render(request,'login.html', context)


def register(request):
    email_form = Emailform()
    if request.method == "POST": # Register
        username = request.POST.get('customerUsername')
        email = request.POST.get('customeremail')
        password = request.POST.get('customerpassword')
        password_1 = request.POST.get('customerConfirmPassword')

        email_form = Emailform(request.POST) # Footer Email
        if email_form.is_valid():
            email_form.save()
            return redirect('index')

        if password == password_1:  # Register
            customer = User.objects.create_user(username , email , password)
            customer.save()
            return redirect('login')
        
      
    context = {
        'email_form': email_form
        }
    return render(request,'register.html',context)




def my_account(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('my-account')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }
    return render(request,'my-account.html', context)





def portfolio_page(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('portfolio-page')
    else:
        email_form = Emailform()

    page = Portfolio.objects.all()
    

    context = {
        'portfolio': page,
        'email_form': email_form
    }
    return render(request, 'portfolio-page.html', context)





# ================== ##### ================== #


def shop_search_results(request):
    email_form = Emailform()
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('shop-search-results')
        

    product_view = Shop.objects.all()

    # price_range = request.GET.get('price_range')
    # if price_range:
    #     min_price, max_price = map(float, price_range.split('-'))
    #     product_view = product_view.filter(price__gte=min_price, price__lte=max_price)

    
    shirt_count = product_view.filter(shirt=True).count()
    jean_count = product_view.filter(jean=True).count()
    woman_count = product_view.filter(woman=True).count()
    ring_count = product_view.filter(ring=True).count()
    bag_count = product_view.filter(bag=True).count()
    service_count = product_view.filter(service=True).count()
    shoe_count = product_view.filter(shoe=True).count()
    elect_count = product_view.filter(elect=True).count()
    cosm_count = product_view.filter(cosm=True).count()


    select_cate = request.GET.get("category")
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        product_view = product_view.filter(price__range=(min_price, max_price))
    if select_cate:
        if select_cate == 'shirt':
            product_view = product_view.filter(shirt=True)
        elif select_cate == 'jean':
            product_view = product_view.filter(jean=True)
        elif select_cate == 'woman':
            product_view = product_view.filter(woman=True)
        elif select_cate == 'ring':
            product_view = product_view.filter(ring=True)
        elif select_cate == 'bag':
            product_view = product_view.filter(bag=True)
        elif select_cate == 'service':
            product_view = product_view.filter(service=True)
        elif select_cate == 'shoe':
            product_view = product_view.filter(shoe=True)
        elif select_cate == 'elect':
            product_view = product_view.filter(elect=True)
        elif select_cate == 'cosm':
            product_view = product_view.filter(cosm=True)


    select_color = request.GET.get("color")
    if select_color:
        product_view = product_view.filter(color=select_color)


    select_size = request.GET.get("size")
    if select_size:
        product_view = product_view.filter(size=select_size)

    selected_brands = request.GET.getlist('brand')
    if selected_brands:
        product_view = product_view.filter(brand__name__in=selected_brands)


    tag_prod = request.GET.get("tag")
    if tag_prod:
        product_view = product_view.filter(tag__name=tag_prod)


    query = request.GET.get('quent')
    if query:
        product_view = product_view.filter(Q(title__icontains=query))

    brands = Brand.objects.all()

    context = {
        'results' : product_view,
        'email_form': email_form,
        'select_cate' : select_cate,
        'shirt_count' : shirt_count,
        'jean_count' : jean_count,
        'woman_count' : woman_count,
        'ring_count' : ring_count,
        'bag_count' : bag_count,
        'service_count' : service_count,
        'shoe_count' : shoe_count,
        'elect_count' : elect_count,
        'cosm_count' : cosm_count,
        'select_color': select_color,
        'select_size' : select_size,
        'tag_prod': tag_prod,
        'selected_brands': selected_brands,
        'brands': brands,
        
        
        
        

    }
    return render(request,'shop-search-results.html',context)





# def cart(request):
#     return render(request,'cart-style1.html')

def checkout(request):
    if request.method == 'POST':
        email_form = Emailform(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect('index')  
    else:
        email_form = Emailform()

    context = {
        'email_form': email_form
        }
    return render(request,'checkout-style1.html',context)

def like(request):
    return render(request,'wishlist-style1.html')

def loyout(request):
    return render(request,'product-layout1.html')

def product_variable(request):
    return render(request,'product-variable.html')