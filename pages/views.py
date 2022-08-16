from django.shortcuts import render, get_object_or_404
from requests import request


def main(request):
     return render(request, 'pages/main.html')