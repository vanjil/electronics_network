from django.contrib import admin
from .models import NetworkUnit, Product

@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'supplier', 'debt', 'created_at')
    search_fields = ('name', 'city')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f"Задолженность очищена у {updated_count} объектов.")

    clear_debt.short_description = "Очистить задолженность у выбранных объектов"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_unit')
    search_fields = ('name', 'model')
