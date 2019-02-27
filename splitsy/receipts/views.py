from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Receipt


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    fields = ['image']


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = Receipt


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt

    def get_success_url(self):
        return reverse('receipts:detail', kwargs={'pk': self.object.pk})
