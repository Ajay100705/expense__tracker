from django.contrib import admin
from .models import Transaction

# admin .site.register(Transaction)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description','amount','created_by',)
                