from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def main(request):
	if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        # Return an error message.

@login_required
def logout(request):
	logout(request)