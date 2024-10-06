from django.conf import settings


def get_paypal_client_id(request):
    return dict(PAYPAL_CLIENT_ID=settings.PAYPAL_CLIENT_ID)
