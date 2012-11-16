from django.db import models


class CmdType(models.Model):
    '''cmd type for proress'''
    cmdTypeName = models.CharField(max_length=32,unique=True,help_text=u"cmdTypeName,Max length 32 chars")
    cmdTypeId = models.IntegerField(primary_key=True,editable=False)
    remark = models.CharField(max_length=100,help_text=u"the cmd remark")
    progressNum = models.IntegerField(editable=True,help_text=u"Must be an integer")
    def __unicode__(self):
        return self.cmdTypeName


class ProgressRateData(models.Model):
    '''the progress data model class'''
    progressId = models.IntegerField(help_text=u'Must be an integer')
    progressName = models.CharField(max_length=32,help_text=u"progressStat,Max length 32 chars")
    progressStat = models.CharField(max_length=32,help_text=u"progressStat,Max length 32 chars")
    #the progress type
    cmdTypeName = models.CharField(max_length=32,help_text=u"cmdTypeName,Max length 32 chars")
    #the exec state succ or faile 
    execStat = models.CharField(max_length=6,help_text=u"execStat,true or false")
    created = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=100,help_text=u"the progress remark")
    
    def __unicode__(self):
        return self.progressName
    
