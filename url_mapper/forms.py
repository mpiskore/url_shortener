from django.core.exceptions import ValidationError
from django.forms import ModelForm
from url_mapper.models import UrlMapper


class UrlMapperForm(ModelForm):
    class Meta:
        model = UrlMapper
        fields = ['original_url']

    def clean(self):
        # check if the url is not yet present in the database
        original_url = self.data['original_url']
        if UrlMapper.objects.filter(original_url=original_url).exists():
            raise ValidationError(
                "There already exists a shortened URL for this original URL.")
        super(UrlMapperForm, self).clean()
