from django.db import models




class ProgressRateData(models.Model):

    progressId = models.IntegerField(help_text='Must be an integer')
    progressName = models.CharField(max_length=32,help_text="progressStat,Max length 32 chars")
    progressStat = models.CharField(max_length=32,help_text="progressStat,Max length 32 chars")
    #the progress type
    cmdType = models.CharField(max_length=6,help_text="cmdType,true or false")
    #
    created = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=100,help_text="the progress remark")
    
    