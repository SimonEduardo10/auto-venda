from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Viatura


# 🏠 DASHBOARD
@login_required
def dashboard(request):
    total_viaturas = Viatura.objects.count()
    viaturas_recentes = Viatura.objects.all().order_by('-id')[:5]

    marcas = Viatura.objects.values('marca').annotate(total=Count('marca'))

    labels = [m['marca'] for m in marcas]
    valores = [m['total'] for m in marcas]

    return render(request, 'viaturas/dashboard.html', {
        'total_viaturas': total_viaturas,
        'viaturas_recentes': viaturas_recentes,
        'labels': labels,
        'valores': valores
    })


# 🔐 LOGIN
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'viaturas/login.html', {
                'error': 'Credenciais inválidas'
            })

    return render(request, 'viaturas/login.html')


# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# 📋 LISTAR
@login_required
def lista_viaturas(request):
    viaturas = Viatura.objects.all()
    return render(request, 'viaturas/lista.html', {'viaturas': viaturas})


# ➕ ADICIONAR
@login_required
def adicionar_viatura(request):

    if request.method == 'POST':
        Viatura.objects.create(
            marca=request.POST['marca'],
            modelo=request.POST['modelo'],
            ano=request.POST['ano'],
            preco=request.POST['preco']
        )
        return redirect('dashboard')

    return render(request, 'viaturas/form.html', {'viatura': None})


# ✏️ EDITAR
@login_required
def editar_viatura(request, id):
    viatura = get_object_or_404(Viatura, id=id)

    if request.method == 'POST':
        viatura.marca = request.POST['marca']
        viatura.modelo = request.POST['modelo']
        viatura.ano = request.POST['ano']
        viatura.preco = request.POST['preco']
        viatura.save()
        return redirect('dashboard')

    return render(request, 'viaturas/form.html', {'viatura': viatura})


# ❌ ELIMINAR (seguro)
@login_required
def eliminar_viatura(request, id):
    viatura = get_object_or_404(Viatura, id=id)

    if request.method == 'POST':
        viatura.delete()

    return redirect('dashboard')