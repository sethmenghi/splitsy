from io import BytesIO

from PIL import Image

from django import forms
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Receipt


class ReceiptCreation(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Receipt
        fields = ('image', 'x', 'y', 'width', 'height')

    def save(self, user, commit=True):
        receipt = super(ReceiptCreation, self).save(commit=False)
        receipt.uploaded_by = user

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(receipt.image)
        cropped_image = image.crop((x, y, w + x, h + y))
        resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)

        resized_image_io = BytesIO()
        resized_image.save(resized_image_io, format='JPEG')
        resized_file = ContentFile(resized_image_io.getvalue())
        receipt.preprocessed_image.save(receipt.preprocessed_img_name, InMemoryUploadedFile(
            resized_file,
            None, '',
            'image/jpeg',
            resized_image.size,
            receipt.image.file.charset
        ), save=False)

        if commit:
            receipt.save()
        return receipt
