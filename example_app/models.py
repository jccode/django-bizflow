from django.db import models

# Create your models here.

class LeaveApplication(models.Model):
    """
    Leave application model
    """
    reason = models.CharField(max_length=100, verbose_name=_('Reason'))
    start_time = models.DateTimeField()

        
        
    
        
        
