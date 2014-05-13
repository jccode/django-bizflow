# -*- coding: utf-8 -*-

from django.contrib import admin
from example_app.models import LeaveApplication


class LeaveApplicationAdmin(admin.ModelAdmin):
    exclude = ('is_agree', )
    list_display = ('proposer', 'reason', 'start_time', 'end_time')



# Register your models here.
admin.site.register(LeaveApplication, LeaveApplicationAdmin)
