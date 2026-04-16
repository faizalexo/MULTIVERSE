from django.shortcuts import render


def home(request):
    toast = request.session.pop('toast', None)  # 🔥 get & remove
    return render(request, 'master/home.html', {'toast': toast})