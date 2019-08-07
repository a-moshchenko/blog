from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    if user.is_superuser:
                        login(request, user)
                        return HttpResponseRedirect('/admin/')
                    else:
                        login(request, user)
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


'''
     if user.is_active:
        # Redirecting to the required login according to user status.
                login(request, user)
                return redirect('/admin/')  # or your url name
            else:
                login(request, user)
                return redirect('')
'''
