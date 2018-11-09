from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "lists of blogs"
	return HttpResponse(response)

def new(request):
	response = "new form to create blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, number):
	response = "blog #"+number
	return HttpResponse(response)

def edit(request, number):
	response = "edit blog#"+number
	return HttpResponse(response)
def destroy(request, number):
	response = "Delete blog#"+number
	return HttpResponse(response)