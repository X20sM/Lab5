from django.shortcuts import render,redirect
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

Users = []
# Create your views here.
def add_User(request):
    global User
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = User(username, password)
        Users.append(User)
        return redirect('People')
    return render(request, 'add_User.html')

def People(request):
    return render(request, 'Users.html', {'Users': Users})