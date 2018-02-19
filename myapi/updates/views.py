from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


from .models import Update

def json_example_view(request):
	data = {
		"count": 100,
		"content": "Some new content",
	}
	return JsonResponse(data)