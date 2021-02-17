from django.shortcuts import render
from .models import Post

from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.mail import send_mail


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
        # do something
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone-number']
        message = request.POST['message']
        send_mail(
            name,
           message,
            email,
            ['to@example.com'],

        )

        context = {
            'name': name,
        }

        return render(request, template_name, context)
    else:
        return render(request, template_name)


class DetailView(DetailView):
    model = Post
    template_name = 'post.html'
