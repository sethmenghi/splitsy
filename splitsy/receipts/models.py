import uuid

from django.urls import reverse
from django.conf import settings
from django.db.models import TextField, ImageField, UUIDField, \
    ForeignKey, CASCADE


from core.models import TimeStampedModel


class Receipt(TimeStampedModel):
    uuid = UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)
    image = ImageField(upload_to='images/raw')
    preprocessed_image = ImageField(upload_to='images/processed', null=True)
    text = TextField(null=True)
    uploaded_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse("receipts:detail", kwargs={"uuid": self.uuid})

    def __str__(self):
        return self.uuid
