# -*- coding: utf-8 -*-

from django.contrib import admin
from example_app.models import LeaveApplication
from fsm_admin.mixins import FSMTransitionMixin


class LeaveApplicationAdmin(FSMTransitionMixin, admin.ModelAdmin):
    # exclude = ['is_agree', ]
    # readonly_fields = ('proposer', )
    list_display = ('proposer', 'reason', 'start_time', 'end_time')

    def get_queryset(self, request):
        qs = super(LeaveApplicationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(proposer=request.user)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'proposer':
            kwargs['initial'] = request.user.id
        return super(LeaveApplicationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['is_agree', 'state', ]
        self.readonly_fields = ()
        if not obj:             # add view
            self.exclude.append('proposer')
        else:
            self.readonly_fields = ('proposer', )
        return super(LeaveApplicationAdmin, self).get_form(request, obj, **kwargs)
        

    def save_model(self, request, obj, form, change):
        if not change:
            obj.proposer = request.user
        obj.save()
        
        

# Register your models here.
admin.site.register(LeaveApplication, LeaveApplicationAdmin)
