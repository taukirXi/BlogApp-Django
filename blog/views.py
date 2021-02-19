from django.shortcuts import render
from .models import Post, Contact

from django.views.generic import ListView
from django.views.generic import DetailView



class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['pub_date']


def about(request):
    context = {
        'head': 'About Me',
        'subhead': 'This is what I Do',
    }
    return render(request, 'about.html', context)


def contact(request):
    template_name = 'contact.html'
    if request.method == 'POST':
        contact = Contact()
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        message = request.POST['message']
        
        contact.name = name
        contact.email = email
        contact.phone = phone_number
        contact.message = message
        contact.save()


        return render(request, template_name, {'name': name})
    else:
        return render(request, template_name)


class DetailView(DetailView):
    model = Post
    template_name = 'post.html'
