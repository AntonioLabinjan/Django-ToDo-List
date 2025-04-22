from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# funkcija koja prima request
# po primitku requesta, dohvaća sve objekte klase task
# vraća renderiranu stranicu task_list.html i dinamički sprema u nju sve ča je spremljeno u varijablu task
'''
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
'''
# New verzija koja još računa count svih zadataka i to dinamički šalje u html
def task_list(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()

    return render(request, 'task_list.html', {
        'tasks': tasks,
        'total_tasks': total_tasks
    })


# funkcija koja prima request
# ako je metoda requesta post, onda iz njega dohvati title i description, spremi ih u pripadne varijable i kreiraj instancu klase task s tim podacima
# ako uspiješ, šalji nas na task_list rutu
# ova funkcija isto tako renderira task_form
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_form.html')

# prima request i pk (nešto ko id I guess)
# dohvati objekt s traženim id-jem ili vrati 404 ako ga nema
# ako smo poslali post zahtjev, provjeri svaki dio taska i vidi ča imamo u post requestu i to spremi
# vrati nas na task_list
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})

# prima request i pk (defintivno je to id
# dohvati objekt s traženim id-jem ili vrati 404 ako ga nema
# ako smo poslali post zahtjev, onda obriši dohvaćeni task
# vrati nas na task_list
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
