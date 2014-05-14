# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import models as auth
from django.utils.translation import ugettext_lazy as _

from django_fsm import FSMIntegerField, transition


# Create your models here.

class State(object):
    """
    Workflow state of LeaveApplication
    """
    DRAFT = 0
    APPROVED_BY_LEADER = 1
    APPROVED_BY_MANAGER = 2
    COMPLETED = 3
    
    CHOICES = (
        (DRAFT, _('draft')), 
        (APPROVED_BY_LEADER, _('approved by leader')), 
        (APPROVED_BY_MANAGER, _('approved by manager')), 
        (COMPLETED, _('completed'))
    )



class LeaveApplication(models.Model):
    """
    Leave application model
    """
    proposer = models.ForeignKey(auth.User, related_name="+", verbose_name=_('Proposer'))
    reason = models.CharField(max_length=100, verbose_name=_('Reason'))
    start_time = models.DateTimeField(verbose_name=_('Leave start time'))
    end_time = models.DateTimeField(verbose_name=_('Leave end time'))
    is_agree = models.BooleanField(default=False, verbose_name=_('Is agreed'))

    state = FSMIntegerField(default=State.DRAFT, verbose_name=_('State'), 
                            choices=State.CHOICES, protected=True)
    
    class Meta:
        verbose_name = _('Leave Application')
        verbose_name_plural = _('Leave Applications')

    def __unicode__(self):
        return "%s - %s" % (self.proposer, self.reason)
        
    
    ########################################
    # Transition condition
    # 

    

    ########################################
    # Workflow transition

    @transition(field=state, source=State.DRAFT, target=State.APPROVED_BY_LEADER)
    def to_leader_approved(self):
        pass


    @transition(field=state, source=State.APPROVED_BY_LEADER,
                target=State.APPROVED_BY_MANAGER)
    def to_manager_approved(self):
        pass


    @transition(field=state, source=[State.APPROVED_BY_LEADER, State.APPROVED_BY_MANAGER],
                target=State.COMPLETED)
    def completed(self):
        pass




