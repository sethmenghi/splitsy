# receipts/tests/test_api.py
import json

from tempfile import NamedTemporaryFile

from PIL import Image

from django.test import TestCase
from django.urls import reverse
from rest_framework.views import status

from splitsy.receipts.models import Receipt
from splitsy.receipts.api.serializers import ReceiptSerializer


class ReceiptAPITests(TestCase):

    def setUp(self):
        self.create_receipt()
        self.create_receipt()

        self.create_read_url = reverse('receipt_rest_api')

    @staticmethod
    def create_receipt(image=None):
        if image is None:
            img_obj = Image.new('RGB', size=(50, 50), color=(155, 0, 0))
            image = NamedTemporaryFile(suffix='.jpg', delete=True)
            img_obj.save(image)
        with open(image.name, 'rb') as data:
            Receipt.objects.get_or_create(image=data)

    @staticmethod
    def _get_test_img():
        image = Image.new('RGB', size=(50, 50), color=(155, 0, 0))
        image_f = NamedTemporaryFile(suffix='.jpg', delete=True)
        image.save(image_f)
        return image_f

    def test_list(self):
        response = self.client.get(self.create_read_url)
        data = json.loads(response.content)
        self.assertEquals(len(data), 2)

        expected = Receipt.objects.all()
        serialized = ReceiptSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        """Test uploading image."""
        test_img = self._get_test_img()
        with open(test_img.name, 'rb') as data:
            response = self.client.post(
                self.create_read_url,
                {'image': data},
                format='multipart'
            )
            response_data = json.loads(response.content)
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
            content = {'id': 3, 'image': data}
            self.assertEquals(content, response_data)
            self.assertEquals(Receipt.objects.count(), 3)
