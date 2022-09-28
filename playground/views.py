from dataclasses import Field
from decimal import Decimal
import decimal
from genericpath import exists
from itertools import count, product
from logging import exception
from multiprocessing import connection
from pyclbr import Function
from turtle import title
from xml.etree.ElementTree import QName
from django.shortcuts import render
from django.db import transaction, connection
from django.db.models.functions import Concat
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Sum, Avg
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Customer, Order, OrderItem, Product
from tags.models import TaggedItem


def say_hello(request):
    # selected_related (1)
    #  prefetch_related (2)
    # queryset = (
    #     Product.objects.prefetch_related("promotions")
    #     .select_related("collection")
    #     .all()
    # )
    # getting the last 5 orders with customers and items(including product)
    # queryset = (
    #     Order.objects.select_related("customer")
    #     .prefetch_related("orderitem_set__product")
    #     .order_by("-placed_at")[:5]
    # )
    # return render(request, "hello.html", {"name": "Mosh", "orders": list(queryset)})
    #
    # queryset = Customer.objects.annotate(
    #     #  CONCAT
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )

    #  Same as above code
    # queryset = Customer.objects.annotate(
    #     #  CONCAT
    #     full_name=Concat(
    #         F("first_name"),
    #         Value(" "),
    #         F("last_name"),
    #     )
    # )
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    return render(
        request,
        "hello.html",
        {
            "name": "Mosh",
        },
    )


# for related titles
# queryset = Product.objects.values("id", "title", "collection__title")

# inventory = price
# queryset = Product.objects.filter(inventory=F("unit_price"))

# products: inventory < 10 AND unit price < 20
# queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)

# products: inventory < 10 OR unit price < 20
# queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

# products: inventory < 10 AND NOT unit price < 20
# queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

# queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
# same as above
# queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
