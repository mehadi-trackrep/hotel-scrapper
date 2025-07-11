from django import forms

class SearchForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)

# django_app/hotels/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from .forms import SearchForm
import os, requests

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://fastapi:8001")

@login_required
def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            response = requests.post(f"{FASTAPI_URL}/api/search_hotels", json={"city": city})
            hotels = response.json()
            return render(request, 'hotels/results.html', {"hotels": hotels})
    else:
        form = SearchForm()
    return render(request, 'hotels/search.html', {"form": form})

@login_required
def bookmark_view(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'hotels/bookmarks.html', {"bookmarks": bookmarks})

@login_required
def add_bookmark(request):
    if request.method == 'POST':
        Bookmark.objects.create(
            user=request.user,
            name=request.POST['name'],
            price=request.POST['price'],
            rating=request.POST['rating'],
            source=request.POST['source'],
            url=request.POST['url']
        )
    return redirect('bookmarks')
