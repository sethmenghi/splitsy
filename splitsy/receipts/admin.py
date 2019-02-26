from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

# from .forms import ReceiptChangeForm, ReceiptCreationForm
from .models import Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):

    list_display = [
        "uuid",
        "image",
        "preprocessed_image",
        "text",
        "uploaded_by"
    ]
    readonly_fields = ('show_url',)

    def show_url(self, instance):
        url = reverse('receipts:detail', kwargs={'pk': instance.pk})
        response = format_html("""<a href="{0}">{0}</a>""", url)
        return response

    show_url.short_description = 'Receipt URL'
    # Displays HTML tags
    # Never set allow_tags to True against user submitted data!!!
    show_url.allow_tags = True
