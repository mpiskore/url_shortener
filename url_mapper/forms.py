from django.forms import ModelForm
from url_mapper.models import UrlMapper


class UrlMapperForm(ModelForm):
    class Meta:
        model = UrlMapper
        fields = ['original_url']
