# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import models as auth
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class LeaveApplication(models.Model):
    """
    Leave application model
    """
    proposer = models.ForeignKey(auth.User, related_name="+", verbose_name=_('Proposer'))
    reason = models.CharField(max_length=100, verbose_name=_('Reason'))
    start_time = models.DateTimeField(verbose_name=_('Leave start time'))
    end_time = models.DateTimeField(verbose_name=_('Leave end time'))
    is_agree = models.BooleanField(default=False, verbose_name=_('Is agreed'))

    class Meta:
        verbose_name = _('Leave Application')
        verbose_name_plural = _('Leave Applications')

    def __unicode__(self):
        return "%s - %s" % (self.proposer, self.reason)
        
        
            
    
        
        
