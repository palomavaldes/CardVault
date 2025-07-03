from django.db import models
from item.models import Item
from decimal import Decimal

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    
    def get_sales_tax_7_percent(self):
        current_total = self.get_total_price()
        SALES_TAX_RATE = Decimal(0.07) # 7%
        return round(current_total * SALES_TAX_RATE, 2)
    
    def final_price(self):
        current_total = self.get_total_price()
        sales_tax = self.get_sales_tax_7_percent()
        return round(current_total + sales_tax, 2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.item.price * self.quantity