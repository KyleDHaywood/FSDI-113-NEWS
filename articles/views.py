from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Article




# Create your views here.
class ArticleCreateView(CreateView):
    template_name="articles/create.html"
    model=Article
    fields= ['title', 'body']

def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name="articles/delete"