from django.shortcuts import render, redirect
from .models import *


class ObjectCreateMixin:
    template = None
    model_form = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'create_form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('posts')
        return render(request, self.template, context={'create_form': bound_form})
