from django.contrib import admin
from .models import NetworkUnit, Product, Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'building_number')
    search_fields = ('country', 'city', 'street')

@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_country', 'get_city', 'supplier', 'debt', 'created_at')
    search_fields = ('name', 'address__city')
    list_filter = ('address__city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f"Задолженность очищена у {updated_count} объектов.")

    clear_debt.short_description = "Очистить задолженность у выбранных объектов"

    def get_country(self, obj):
        return obj.address.country
    get_country.short_description = 'Страна'

    def get_city(self, obj):
        return obj.address.city
    get_city.short_description = 'Город'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'display_network_units')
    search_fields = ('name', 'model')
    filter_horizontal = ('suppliers',)  # Позволяет выбирать поставщиков через M2M

    def display_network_units(self, obj):
        return ", ".join([unit.name for unit in obj.suppliers.all()])
    display_network_units.short_description = 'Поставщики'