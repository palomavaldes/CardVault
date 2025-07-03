from django.db import models
from item.models import Item
from decimal import Decimal

class Order(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    postal_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_sales_tax_7_percent(self):
        current_total = self.get_total_cost()
        SALES_TAX_RATE = Decimal(0.07) # 7%
        return round(current_total * SALES_TAX_RATE, 2)
    
    def final_price(self):
        current_total = self.get_total_cost()
        sales_tax = self.get_sales_tax_7_percent()
        return round(current_total + sales_tax, 2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_cost(self):
        return self.price * self.quantity