from django.contrib import admin
from .models import m_donation

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display=("id","user_id_id","brand_name","generic_name","type","quantity","manufacturing_date","expiry_date","description","availability_status")
    search_fields = ("brand_name","generic_name","type","quantity","manufacturing_date","expiry_date","description")
    ordering = ('id',)
    list_filter = ("brand_name","generic_name","type","availability_status")
    filter_horizontal = ()

admin.site.register(m_donation,DonationAdmin)