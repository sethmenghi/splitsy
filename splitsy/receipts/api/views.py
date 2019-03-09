from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from splitsy.receipts.models import Receipt

from .serializers import ReceiptSerializer


class ReceiptListCreateAPIView(ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    lookup_field = 'uuid'  # Don't use Receipt.id!


class ReceiptRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ReceiptSerializer
    lookup_field = 'uuid'  # Don't use Receipt.id
