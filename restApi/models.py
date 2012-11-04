from django.db import models




class ProgressRateData(models.Model):

    progressId = models.IntegerField(help_text='Must be an integer')
    progressName = models.CharField(max_length=32,help_text="progressStat,Max length 32 chars")
    progressStat = models.CharField(max_length=32,help_text="progressStat,Max length 32 chars")
    created = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=100,help_text="the progress remark")
    
    