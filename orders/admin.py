from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["item"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "address", "city", "state", "postal_code"]
    inlines = [OrderItemInline]
    readonly_fields=("created_at",)
    