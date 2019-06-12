from django.db import models


class ShopBalanceQuerySet(models.QuerySet):
    def paid_price(self):
        """
        Taking the total price for purchased item during balance period.
        Purchased item's status is in ['start', 'ready', 'paid']
        
        :EX:
        return blash...blash... .annotate(
            paid_price=['Q1-1']
        )
        """
        raise NotImplementedError

    def cancelled_price(self):
        """
        Taking the total price for cancelled item during balance period.
        Cancelled item's status is 'cancelled'

        :EX:
        return blash...blash... .annotate(
            cancelled_price=['Q1-2']
        )
        """
        raise NotImplementedError

    def pending_price(self):
        """
        Find the difference between the balance within period and 
        the price of the purchase completed within period.
        
        This price is the balance amount that can be exhausted 
        within the balance period.

        :EX:
        return blash...blash... .annotate(
            pending_price=['Q1-3']
        )
        """
        raise NotImplementedError

    def contract_count(self):
        """
        Number of contracts in the balance period.

        :EX:
        return blash...blash... .annotate(
            contract_count=['Q1-4']
        )
        """
        raise NotImplementedError

    def accumulate_balance(self):
        raise NotImplementedError