from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, User
from .forms import PersonForm, UserForm
from django.contrib.auth.decorators import login_required


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})


@login_required
def persons_create(request):
    form = PersonForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'persons_create.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'persons_create.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    return render(request, 'persons_delete_confirm.html', {'person': person})


@login_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


@login_required
def users_create(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('users_list')
    return render(request, 'users_create.html', {'form': form})


@login_required
def users_update(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('users_list')
    return render(request, 'users_create.html', {'form': form})


@login_required
def users_delete(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)

    if request.method == 'POST':
        user.delete()
        return redirect('users_list')
    return render(request, 'users_delete_confirm.html', {'user': user})