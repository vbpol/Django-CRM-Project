from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import Foo
class FooCreateView(CreateView):
    model = Foo
    fields = '__all__'