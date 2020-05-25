from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def Home(request):
    return render(request,'testapp/home.html')
def Index(request):

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mail'):
            post = Post()
            print(type(post))
            post.name = request.POST.get('name')
            post.mail = request.POST.get('mail')
            post.mnumber = request.POST.get('mnumber')
            post.msg = request.POST.get('msg')
            post.save()
            return render(request,'testapp/index.html')


        else:
            return render(request, 'testapp/index.html')
    return render(request,'testapp/index.html')





from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CoffeListView(ListView):
    model = Post

class CoffeDetailView(DetailView):
    model = Post