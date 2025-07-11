from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from .forms import SearchForm
import os
import requests

# Base URL for FastAPI service
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://fastapi:8001")

@login_required
def search_view(request):
    """Handles hotel search and calls FastAPI to get results."""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            try:
                response = requests.post(
                    f"{FASTAPI_URL}/api/search_hotels",
                    json={"city": city},
                    timeout=60
                )
                hotels = response.json()
            except Exception as e:
                hotels = []
                print(f"FastAPI error: {e}")
            return render(request, 'hotels/results.html', {"hotels": hotels})
    else:
        form = SearchForm()
    return render(request, 'hotels/search.html', {"form": form})

@login_required
def bookmark_view(request):
    """Shows all bookmarks of the current user."""
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'hotels/bookmarks.html', {"bookmarks": bookmarks})

@login_required
def add_bookmark(request):
    """Adds a hotel to the user's bookmarks."""
    if request.method == 'POST':
        Bookmark.objects.create(
            user=request.user,
            name=request.POST.get('name', ''),
            price=request.POST.get('price', ''),
            rating=request.POST.get('rating', ''),
            source=request.POST.get('source', ''),
            url=request.POST.get('url', '')
        )
    return redirect('bookmarks')