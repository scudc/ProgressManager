from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse
from models import ProgressRateData


class MyModelResource(ModelResource):
    model = ProgressRateData
    fields = ('progressId', 'progressStat', 'remark', 'url')
    ordering = ('created',)

    def url(self, instance):
        return reverse('model-resource-instance',
                       kwargs={'id': instance.id},
                       request=self.request)