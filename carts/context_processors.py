from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        cart_count = 0
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])

            for item in cart_items:
                cart_count += item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
        return dict(cart_count=cart_count)
