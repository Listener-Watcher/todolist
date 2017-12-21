from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .models import *
from .forms import *


# Create your views here.
def index(request):
	items = Item.objects.all()
	context={
		'items':items
	}
	
	return render(request,'index.html',context)

def details(request,id):
	item = Item.objects.get(id=id)
	context={
		'item':item
	}
	return render(request,'details.html',context)
	
def edit(request):
	if(request.method=='POST'):
		form = EditForm(request.POST)
		
		if form.is_valid():
			item_text=form.cleaned_data['text']
			item_title=form.cleaned_data['title']
			item = Item.objects.get(title=item_title)
			item.text=item_text
			item.save()
			return redirect('/todolist/index')
		else:
			return redirect('/todolist/edit')
	else:
		form = EditForm
	return render(request,'edit.html',{'form':form})

def marked(request):
	if(request.method=='POST'):
		form = EditFinishedForm(request.POST)
		
		if form.is_valid():
			item_marked=form.cleaned_data['finished']
			item_title=form.cleaned_data['title']
			item = Item.objects.get(title=item_title)
			item.finished=item_marked
			item.save()
			return redirect('/todolist/index')
		else:
			return redirect('/todolist/marked')
	else:
		form = EditFinishedForm
	return render(request,'marked.html',{'form':form})

def changetime(request):
	if(request.method=='POST'):
		form = EditTimeForm(request.POST)
		
		if form.is_valid():
			item_time=form.cleaned_data['createdTime']
			item_title=form.cleaned_data['title']
			item = Item.objects.get(title=item_title)
			item.createdTime=item_time
			item.save()
			return redirect('/todolist/index')
		else:
			return redirect('/todolist/changetime')
	else:
		form = EditTimeForm
	return render(request,'changetime.html',{'form':form})
def delete(request):
	if(request.method=='POST'):
		form = DeleteForm(request.POST)
		
		if form.is_valid():
			item_title = form.cleaned_data['title']
			item = Item.objects.get(title=item_title)
			item.delete()
			return redirect('/todolist/index')
		else:
			return redirect('/todolist/delete')
	else:
		form = DeleteForm()
	return render(request,'delete.html',{'form':form})

def add(request):
	if(request.method =='POST'):
		form =AddForm(request.POST)
		
		if form.is_valid():
			title=form.cleaned_data['title']
			text=form.cleaned_data['text']
			createdTime = form.cleaned_data['createdTime']
			priority = form.cleaned_data['priority']
			finished = form.cleaned_data['finished']
			item = Item(title=title,text=text,createdTime=createdTime,priority=priority,finished=finished)
			item.save()
			return redirect('/todolist/index')
		else:
			return redirect('/todolist/add')
	else:
		form = AddForm()
	return render(request,'add.html',{'form':form})

def status_report(request):
	todo_listing = []
	for todo_list in List.objects.all():
		todo_dict = {}
		todo_dict['list_object']=todo_list
		todo_dict['item_count']=todo_list.item_set.count()
		todo_dict['items_complete']=todo_list.item_set.filter(finished=True).count()
		todo_dict['percent_complete']=int(float(todo_dict['items_complete'])/todo_dict['item_count']*100)
		todo_listing.append(todo_dict)
		return render(request,'status_report.html',{'todo_listing':todo_listing})
