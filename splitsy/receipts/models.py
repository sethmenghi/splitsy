import os
import uuid

from django.urls import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.db import models


from splitsy.core.models import TimeStampedModel


class Receipt(TimeStampedModel):
    # slug = models.SlugField(unique=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)
    image = models.ImageField(upload_to='images/raw')
    preprocessed_image = models.ImageField(upload_to='images/processed', null=True)
    text = models.TextField(null=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receipts', on_delete=models.CASCADE)

    @property
    def preprocessed_img_name(self):
        if self.preprocessed_image.name is None:
            if self.image.name is None:
                return None
            base, filename = os.path.split(self.image.name)
            return 'preprocessed_' + filename
        return os.path.split(self.preprocessed_image.name)[-1]

    def image_tag(self):
        return mark_safe('<img src="%s" class="img-thumbnail">' % (self.image.url))

    def preprocessed_image_tag(self):
        return mark_safe('<img src="%s" class="img-thumbnail">' % (self.preprocessed_image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse("receipts:detail", kwargs={"uuid": self.uuid})

    def __str__(self):
        return str(self.pk)
