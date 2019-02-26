from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .models import Receipt


class ReceiptListView(ListView):
    model = Receipt


class ReceiptDetailView(DetailView):
    model = Receipt


class ReceiptResultsView(ReceiptDetailView):
    template_name = 'receipts/results.html'


class ReceiptUpdateView(UpdateView):
    model = Receipt

    def get_success_url(self):
        return reverse('receipts:detail', kwargs={'pk': self.object.pk})
