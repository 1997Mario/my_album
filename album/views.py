from django.shortcuts import render
from album.models import Category, Photo 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.


def first_view(request):
 return HttpResponse('<h1>Esta es mi primera vista!</h1>') 

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html',context)

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)


from django.views.generic import ListView, DetailView

class PhotoListView(ListView):
    model = Photo

class PhotoDetailView(DetailView): 
    model = Photo

def base(request):
 return render(request, 'base.html')



class PhotoUpdate(UpdateView):
 model = Photo
 fields='__all__'

class PhotoCreate(CreateView):
 model = Photo
 fields='__all__'
 
class PhotoDelete(DeleteView):
 model = Photo
 success_url = reverse_lazy('photo-list')

