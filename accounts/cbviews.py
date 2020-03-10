import django.views.generic as views
from .models import User
# 3. Create views for: 
# list of all users, 
# viewing, 
# adding, 
# editing 
# deleting a single user


class UserList(views.ListView):
    model = User
    template_name = 'accounts/list.html'


class UserDetail(views.DetailView):
    model = User
    template_name = 'accounts/detail.html'


class AddUser(views.CreateView):
    model = User
    template_name = 'accounts/add_user.html'
    

class EditUser(views.UpdateView):
    model = User
    template_name = 'accounts/edit_user.html'


class DeleteUser(views.DeleteView):
    model = User
    template_name = 'accounts/delete_user.html'


