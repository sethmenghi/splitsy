from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Receipt
from .forms import ReceiptCreation


@login_required
def receipt_list(request):
    user = request.user
    if request.method == 'POST':
        form = ReceiptCreation(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=user)
            return redirect('receipts:list')
    else:
        form = ReceiptCreation()
    receipts = Receipt.objects.filter(uploaded_by=user)
    return render(request, 'receipts/receipt_list.html', {'form': form, 'receipts': receipts})


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    fields = ['image']


# class ReceiptListView(LoginRequiredMixin, ListView):
#     model = Receipt


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = Receipt


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt
    fields = ['image', 'text']

    def get_success_url(self):
        return reverse('receipts:detail', kwargs={'pk': self.object.pk})


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt

    def get_success_url(self):
        return reverse('receipts:list')
