from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def validate_link(url):
    if "www.linkedin.com" in url:
        return True
    elif "www.ziprecruiter.com" in url:
        return True
    elif "www.indeed.com" in url:
        return True
    elif "www.glassdoor.com" in url:
        return True
    else:
        return False
