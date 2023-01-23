from django.contrib import admin
from .models import NGOModel,DonorModel,DonationModel,DonationRequestModel

class NGOModelAdmin(admin.ModelAdmin):
    list_display=['ngo_id','ngo_name','username','password','address','phone_number','started_in','documents']
admin.site.register(NGOModel,NGOModelAdmin)

class DonorModelAdmin(admin.ModelAdmin):
    list_display=['donar_id','ngo_id','donar_name','username','password','email_id','phone_number','address']
admin.site.register(DonorModel,DonorModelAdmin)

class DonationModelAdmin(admin.ModelAdmin):
    list_display=['donation_id','donar_id','ngo_id','donation_type','amount','donation_date']
admin.site.register(DonationModel,DonationModelAdmin)

class DonationRequestModelAdmin(admin.ModelAdmin):
    list_display=['request_id','amount','donar_id','ngo_id','donation_end_date']
admin.site.register(DonationRequestModel,DonationRequestModelAdmin)
