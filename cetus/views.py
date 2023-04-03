from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.validators import RegexValidator
from .models import *
import random



Customer_session_nm=None
Customer_session_id=None


def index(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    cat=Category.objects.all()
    product=Product.objects.filter().order_by('-id')[:4]
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/index.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'cat':cat,'product_list':product,'email':Customer_session_nm[0]}); 
    return render(request,'cetus/index.html',{'cat':cat,'product_list':product}); 

def productbycategory(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    category=Category.objects.get(id=id)
    cat=Category.objects.all()
    print("Name",category)
    products=Product.objects.filter(Category=category)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/productcat.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'cl':cat,'pl':products,'category':category}); 

    return render(request,'cetus/productcat.html',{'cl':cat,'pl':products,'category':category}); 
        

def about(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'cetus/about.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name})

    return render(request,'cetus/about.html')
   

def contact(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/contact.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name})

    return render(request,'cetus/contact.html')

def register(request):
    return render(request,'cetus/register.html');  

def signin(request):
    return render(request,'cetus/login.html'); 

def registersubmit(request):
    Customer_session_nm = None
    Customer_session_id = None
    data=Register.objects.all()
    if request.method == "POST":
        name=request.POST.get('Name','')
        email=request.POST.get('Email','')
        password=request.POST.get('Password','')
        cpassword=request.POST.get('CPassword','')
        for info in data:
            if info.Email ==email:
                messages.warning(request, 'email already exists.')
                return redirect('register')

        if  password != cpassword:
            messages.error(request, 'Password and Confirm Passsword Must be Same')    
            return redirect('register') 
        if name=="" or email=="" or password=="":
            messages.error(request, 'Please Enter Required Field')    
            return redirect('register')    
        else:
            i=Register(Name=name,Email=email,Password=password)
            i.save()
            name=" "
            messages.add_message(request, messages.INFO, 'Thanks For Register YourSelf.')
    return redirect('login')


def login(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
        print(Customer_session_id)
    user = Customer_session_id

    if request.method=='POST':   
        email=request.POST['Email']
        password=request.POST['Password']

        Customer_name=Register.objects.filter(Email__contains=email,Password__contains=password).values_list('Email', 'id').first()
        if Customer_name is not None:
                request.session['name'] = Customer_name
                request.session['id'] = Customer_name[1]
                return redirect('cust_login1')

        else:
            messages.error(request, 'Please Enter Valid UserName And Password.')
            return redirect('login')  
                  
    return render(request,'cetus/login.html')    

def cust_login1(request):
    Customer_session_nm = None
    Customer_session_id = None
    global str_num
    num=random.randrange(1121,9899)
    str_num=str(num)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
    user = Customer_session_id
    
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
       
    else:
        
        return render(request,'cetus/login.html',{})
       
    return render(request,'cetus/sendrequirnment.html',{'Customer_session_nm':Customer_session_nm ,  'name':Register.objects.get(id=user).Name,'img':str_num,'email':Customer_session_nm[0]})



def sendrequirnment(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    print("user",user)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    global str_num
    num=random.randrange(1121,9899)
    str_num=str(num)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/sendrequirnment.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'img':str_num,'email':Customer_session_nm[0]});
    return redirect('register')     


def requirnmentsubmit(request):
    global str_num
    if request.method == 'POST':
        name=request.POST.get('name','')
        company=request.POST.get('company','')
        designation=request.POST.get('designation','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        pincode=request.POST.get('pincode','')
        state=request.POST.get('state','')
        country=request.POST.get('country','')
        mobile=request.POST.get('mobile','')
        telephone=request.POST.get('telephone','')
        email=request.POST.get('email','')
        modelno=request.POST.get('modelno','')
        code=request.POST.get('txtcaptcha','')
        if name == "" or company == "" or designation == "" or address == "" or city == "" or pincode == "" or state == "" or country == "" or mobile == "" or telephone == "" or email == "" or modelno == "":
            messages.error(request, 'Please Enter Required Field')
            return redirect('sendrequirnment')

        elif str(code)==str_num :
            i=Requirnment(Name=name,Company=company,Designation=designation,Address=address,City=city,Pincode=pincode,State=state,Country=country,Mobile=mobile,Telephone=telephone,Email=email,Modelno=modelno)
            i.save()
            return redirect('myrequirement')
        
        else:
                messages.warning(request, 'Please Enter Valid CAPTCHA.')
                return redirect('sendrequirnment')
    else:
            return redirect('sendrequirnment')

def contactsubmit(request): 
    cat=Category.objects.all()
    product=Product.objects.filter().order_by('-id')[:4]
    if request.method == "POST":
        name=request.POST.get('Name','')
        email=request.POST.get('Email','')
        subject=request.POST.get('Subject','')
        message=request.POST.get('Message','')
        if name=="" or email=="" or subject=="" or message=="":
            messages.error(request, 'Please Enter Required Field')
            return redirect('contact')
        else:
            i=Contact(Name=name,Email=email,Subject=subject,Message=message)
            i.save()
            name=" "
            messages.add_message(request, messages.INFO, 'Thanks For Connect With Cetus.')
    return redirect('index')
def product(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cat=Category.objects.all()
    product=Product.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/products.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'cat_list':cat,'product_list':product});

    return render(request,'cetus/products.html',{'cat_list':cat,'product_list':product});


def productdetail(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    product=Product.objects.get(id=id)
    cat=product.Category
    relatedproduct=Product.objects.filter(Category=cat)[:12]
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/productdetails.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'product':product,'relatedproduct':relatedproduct}); 
    return render(request,'cetus/productdetails.html',{'product':product,'relatedproduct':relatedproduct}); 


def brochurelist(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    data=brochure.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/brochure.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'data':data}); 
    return render(request,'cetus/brochure.html',{'data':data});  

def images(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    data=brochure.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/eventimage.html',{'Customer_session_nm':Customer_session_nm ,'name':Register.objects.get(id=user).Name,'data':data}); 
    return render(request,'cetus/eventimage.html',{'data':data}); 

def logout(request):

    
    try:
        del request.session['name']
        return redirect('index',)
    except:
      pass
    return redirect('index')



def myrequirement(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    user1 = Register.objects.get(id=user)
    email=user1.Email
    print(email)
    requirement=Requirnment.objects.raw('SELECT * FROM cetus_Requirnment WHERE  Email = %s',[email])
    no=len(requirement)
    print("no",no)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'cetus/myrequirnment.html',{'Customer_session_nm':Customer_session_nm ,  'name':Register.objects.get(id=user).Name,'requirement':requirement,'no':no}); 
    return redirect('index')
def deleterequirement(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    d=""
    n=""
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cus_list=Register.objects.all()
    user1 = Register.objects.get(id=user)
    
    req=Requirnment.objects.get(id=id)
    req.delete()
  
    return redirect('myrequirement')
    
def subscribe(request):
    data=newsletter.objects.all()
    print("sub",data)
    if request.method == 'POST':
        mail=request.POST.get('txtEmail','')
        m=newsletter(mail=mail)
        for info in data:
            if info.mail ==mail:
                messages.warning(request, 'You already Subscribe for Newsletter.')
                return redirect('index')
    if mail=="":
        messages.error(request, 'Please Enter Email id for subscribe')
        return redirect('index') 
    else:
        m.save()
    return redirect('index')    

