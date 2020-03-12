import django.views.generic as views
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .models import User
from .forms import UserForm


class UserList(views.ListView):
    queryset = User.objects.order_by('date_joined')
    template_name = 'accounts/list.html'
    context_object_name = 'users'
    paginate_by = 4


class UserDetail(views.DetailView):
    model = User
    template_name = 'accounts/detail.html'
    context_object_name = 'user'

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

    def get_success_url(self):
        username = self.object.username
        return reverse('accounts:detail', kwargs={'username': username})

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username) 


class DeleteUser(views.DeleteView):
    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('accounts:list')

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username) 



