from django.contrib import admin
from bidding_app.models import Staff, Item, Bid
# Register your models here.


class BidAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)


admin.site.register(Staff)
admin.site.register(Item)
admin.site.register(Bid, BidAdmin)
