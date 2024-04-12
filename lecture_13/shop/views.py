import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from django.views.decorators.csrf import csrf_exempt


# def categories_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         categories_data = []
#
#         for category in categories:
#             data = {
#                 'id': category.id,
#                 'name': category.name,
#                 'description': category.description,
#             }
#             categories_data.append(data)
#         return JsonResponse(data={'categories': categories_data}, status=200)
#
#     if request.method == 'POST':
#         pass

@csrf_exempt
def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(data={'categories': serializer.data}, status=200)

    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        else:
            return JsonResponse(data=serializer.errors, status=400)

    return JsonResponse(data={'errors': 'Unsupported request type'}, status=400)


@csrf_exempt
def category_view(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return JsonResponse(data={'message': 'Category not found'}, status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(data=serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        else:
            return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        category.delete()
        return JsonResponse(data={'message': 'Category successfully deleted'}, status=200)

