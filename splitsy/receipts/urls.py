from django.conf.urls import url
from . import views

app_name = "receipts"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.ReceiptListView.as_view(),
        name='list'
    ), url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.ReceiptDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.ReceiptUpdateView.as_view(),
        name='update'
    ), url(
        regex=r'^create/$',
        view=views.ReceiptCreateView.as_view(),
        name='create'
    ),
]
