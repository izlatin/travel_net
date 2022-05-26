from django.shortcuts import redirect
from django.urls import reverse


def feed(request):
    # return render(request, 'homepage/feed.html')
    return redirect(reverse('publications:publication_list'))
