from django.db import models

from apps.shop.models import ShopItem


class Payment(models.Model):
    STATUS_START = 0
    STATUS_READY = 1
    STATUS_PAID = 2
    STATUS_CANCELLED = 3
    STATUS_REFUND = 4
    STATUS_TYPE = (
        (STATUS_START, 'start'),
        (STATUS_READY, 'ready'),
        (STATUS_PAID, 'paid'),
        (STATUS_CANCELLED, 'cancelled'),
        (STATUS_REFUND, 'refund'),
    )

    shop_item = models.ForeignKey(
        ShopItem,
        on_delete=models.CASCADE
    )
    item_count = models.IntegerField(
        default=1
    )
    status = models.IntegerField(
        choices=STATUS_TYPE,
        default=STATUS_START
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'payments'
