from django.db import models

from .managers import (
    ShopBalanceQuerySet,
)


class Shop(models.Model):
    name = models.CharField(
        max_length=20
    )
    is_active = models.Boolean(
        default=True,
        help_text="User can only see active shop"
    )

    class Meta:
        db_table = 'shops'

    def __str__(self):
        return self.name


class ShopItem(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100
    )
    price = models.IntegerField(
        default=0
    )

    class Meta:
        db_table = 'shop_items'


class ShopBalance(models.Model):
    """
    Balance model that shop has. The shop balance may have
    serveral balances depending on the type of contract.
    The shop can only sell shop items within shop balance.
    """
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE
    )
    price = models.IntegerField(
        'Item Price',
        default=0
    )
    start_date = models.DateTimeField(
        help_text="Item can only sell in start/end date duration."
    )
    end_date = models.DateField(
        help_text="Item can only sell in start/end date duration."
    )
    enable_accumulate = models.Boolean(
        default=True,
        help_text='Checks whether remaining balance will be accumulated.'
    )

    objects = ShopBalanceQuerySet.as_manager()

    class Meta:
        db_table = 'shop_balances'


class ShopContract(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(
        help_text="Valid contract on date."
    )
    end_date = models.DateField(
        help_text="Valid contract on date."
    )

    class Meta:
        db_table = 'shop_contracts'
