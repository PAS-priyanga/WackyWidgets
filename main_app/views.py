from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm

def index(request):
  widgets = Widget.objects.all()
  total_quantity = sum(widget.quantity for widget in widgets)
  add_widget_form = WidgetForm()
  return render(request, "index.html",{"widgets": widgets, "total_quantity": total_quantity, "add_widget_form": add_widget_form})

def add_Widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save();
  return redirect('index')

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'