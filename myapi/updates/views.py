import json

from django.core.serializers import serialize
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


from .models import Update
from .mixins import JsonResponseMixin

def json_example_view(request):
	data = {
		"count": 100,
		"content": "Some new content",
	}
	return JsonResponse(data)


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
			"count": 100,
			"content": "Some new content",
		}
		return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
			"count": 100,
			"content": "Some new content",
		}
		return self.render_to_json_response(data)


class SerializedDetailView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		json_data = obj.serialize()
		return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all()
		json_data = Update.objects.all().serialize()
		return HttpResponse(json_data, content_type='application/json')