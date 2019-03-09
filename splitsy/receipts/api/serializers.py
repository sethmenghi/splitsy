from rest_framework import serializers

from ..models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):

    uploaded_by = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Receipt
        fields = ['uuid', 'image']

#     def create(self, validated_data):
        # receipt = Receipt(
        #     image=validated_data.get('data', None)
        # )

        # receipt.save()
        # return receipt