from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base.html")


def search(request):

    searchResults = request.GET.get("searchResults") or "Not Found"
    
    return render(request, "search.html",{"sec": searchResults})
