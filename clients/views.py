from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.http import HttpResponse
import openpyxl







def export_clients_excel(request):
    # إنشاء ملف Excel جديد
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Clients"

    # العناوين
    ws.append(["الاسم", "كاش", "هوا", "ملاحظات", "تاريخ الإضافة"])

    # البيانات
    clients = Client.objects.all()
    for c in clients:
        ws.append([c.name, c.cash, c.hawa, c.note or "", c.created_at.strftime("%Y-%m-%d %H:%M")])

    # إعداد الاستجابة
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="clients.xlsx"'
    wb.save(response)
    return response

def client_list(request):
    clients = Client.objects.all()
    total_cash = sum(c.cash for c in clients)
    total_hawa = sum(c.hawa for c in clients)
    total = total_cash + total_hawa

    # إضافة عميل جديد
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'clients/client_list.html', {
        'clients': clients,
        'form': form,
        'total_cash': total_cash,
        'total_hawa': total_hawa,
        'total': total,
    })

def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form, 'client': client})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/delete_confirm.html', {'client': client})
