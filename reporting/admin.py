# from django.contrib import admin
# from .models import Orders

# admin.site.register(Orders)


from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('id', 'amount', 'description', 'created_time')

    # Fields you can filter by (sidebar)
    list_filter = ('created_time',)

    # Fields you can search by (search bar)
    search_fields = ('amount', 'description')

    # Fields that will be editable directly from the list view
    list_editable = ('amount',)

    # How many records per page in list view
    list_per_page = 25

    # Date hierarchy navigation (top-right)
    date_hierarchy = 'created_time'

    # Optional: ordering of records by default
    ordering = ('-created_time',)

    # Optional: read-only fields in the detail view
    # readonly_fields = ('created_item',)  # Uncomment if you want

    # Optional: custom display for long text (shorten description)
    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    # You can include short_description in list_display if desired:
    # list_display = ('id', 'amount', 'short_description', 'created_item')
