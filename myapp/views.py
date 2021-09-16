from django.shortcuts import redirect, render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Contact

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        upload_file=request.FILES['image']

        findContact=Contact.objects.filter(email=email,phone=phone)
        if findContact:
            return render(request,'contactform.html',{'message':"Contact Already Present!!"})
        else:
            contact=Contact(name=name,email=email,phone=phone,image=upload_file)
            contact.save()
        return render(request,'contactform.html',{'message':"Contact Successfully Added!!"})
    return render(request,'contactform.html')

def get_all_contacts(request):
    try:
        contacts=get_list_or_404(Contact)
    except Contact.DoesNotExist:
        return render(request,'base.html')
    return render(request,'contactlist.html',{'contacts':contacts})

def contact_card(request,id):
    contact=get_object_or_404(Contact,pk=id)
    return render(request,'contactcard.html',{'contact':contact})

def delete_contact(request,id):
    contact=get_object_or_404(Contact,pk=id)
    contact.delete()
    return redirect('/')
    #contacts=Contact.objects.all()
    #return render(request,'contactlist.html',{'contacts':contacts})

def edit_contact(request,id):
    contact=get_object_or_404(Contact,pk=id)
    return render(request,'contactedit.html',{"contact":contact})

def edit(request,id):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        contact=get_object_or_404(Contact,pk=id)
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.save()
        return redirect('/')

def change_photo(request,id):
    return render(request,'imagechange.html',{'id':id})

def change_image(request,id):
    if request.method=="POST":
        upload_photo=request.FILES['image']
        contact=get_object_or_404(Contact,pk=id)
        contact.image=upload_photo
        contact.save()
        return redirect('/')
