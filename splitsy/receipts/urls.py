from django.conf.urls import url

from splitsy.receipts.api import views as api_views

from . import views

app_name = "receipts"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.receipt_list,
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
    ), url(
        regex=r'^(?P<pk>\d+)/delete/$',
        view=views.ReceiptDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'^api/$',
        view=api_views.ReceiptListCreateAPIView.as_view(),
        name='receipt_rest_api'
    ),
    # /receipt/api/:slug/
    url(
        regex=r'^api/(?P<uuid>[-\w]+)/$',
        view=api_views.ReceiptRetrieveUpdateDestroyAPIView.as_view(),
        name='receipt_rest_api'
    )
]
