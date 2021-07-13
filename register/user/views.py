from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SigninForm
# Create your views here.

@login_required
def profile(request):
    return render(request, 'user/profile.html')


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form':form})
