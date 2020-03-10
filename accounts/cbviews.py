import django.views.generic as views
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import User
from .forms import UserForm
# 3. Create views for: 
# list of all users, 
# viewing, 
# adding, 
# editing 
# deleting a single user
# TODO check template_name_suffix

class UserList(views.ListView):
    model = User
    template_name = 'accounts/list.html'
    paginate_by = 10

class UserDetail(views.DetailView):
    model = User
    template_name = 'accounts/detail.html'

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username) 


class AddUser(views.CreateView):
    model = User
    template_name = 'accounts/add_user.html'
    form_class = UserForm 

class EditUser(views.UpdateView):
    model = User
    template_name = 'accounts/edit_user.html'
    form_class = UserForm

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username) 


class DeleteUser(views.DeleteView):
    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('list')

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username) 



