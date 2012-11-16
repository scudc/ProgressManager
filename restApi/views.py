from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import ProgressRateData
from django.conf import settings
import json

context = {"STATIC_URL":settings.STATIC_URL} 
g_state_length = 10
#get the request by progress id
def getProgress(request):
    progressIdList = request.GET.get('idList').split(",")
    cmdTypeName = request.GET.get('cmd')
    progressDataSet = []
    
    for pro_id in progressIdList:
            progressData = {}
            if len(pro_id) != 0:
                progressList = ProgressRateData.objects.order_by('created').filter(progressId=pro_id,cmdTypeName=cmdTypeName)
                if len(progressList) < 1:
                    continue
                progress = progressList[0]
                progressData['progressId'] = progress.progressId
                progressData['progressName'] = progress.progressName
            progressDataSet.append(progressData)
    context['progressDataSet'] = progressDataSet
    return render_to_response('restApi/progress.html',context)


#get the data of progress data
def getProgressBarData(request):
    progressIdList = request.GET.get('idList').split(",")
    progressDataSet = []
    
    for pro_id in progressIdList:
        progressData = {}
        if len(pro_id) != 0:
            stateLength = ProgressRateData.objects.filter(progressId=pro_id).count()
            progressBarData = float(stateLength) / float(g_state_length)
            progressBarData = str(progressBarData * 100) + "%"
            progressData['instanceId'] = pro_id.encode('utf-8')
            progressData['progressBarData'] = progressBarData
        progressDataSet.append(progressData)
    if request.is_ajax():
        #message = '[{"instanceId":"1","progressBarData":"20%"},{"instanceId":"2","progressBarData":"20%"}]'
        mimetype = 'application/javascript'
        return HttpResponse(json.dumps(progressDataSet),mimetype)
    else:
        return HttpResponse(status=400)
    
    
        

