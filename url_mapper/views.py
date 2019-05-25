from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView

from url_mapper.forms import UrlMapperForm
from url_mapper.models import UrlMapper


class UrlDetail(DetailView):
    template_name = "url_mapper/detail.html"
    model = UrlMapper

    def get_object(self):
        # remove unnecessary backslashes and exclamation mark from url
        shortened_url = self.request.path[2:-1]
        return get_object_or_404(UrlMapper, shortened_url=shortened_url)


class HomePage(FormView):
    template_name = "url_mapper/home.html"
    form_class = UrlMapperForm

    def form_invalid(self, form):
        # redirect to already existing url
        try:
            existing_url = UrlMapper.objects.get(original_url=form.data["original_url"])
            self._prepare_message(existing_url)
            return redirect("result", shortened=existing_url.shortened_url)
        except ObjectDoesNotExist:
            messages.add_message(
                self.request,
                messages.ERROR,
                "You have no users in the database. You can add them "
                "by running python manage.py create_fake_users N "
                "where N is the number of users.",
            )
            return redirect("home")

    def form_valid(self, form):
        random_user = User.objects.order_by("?").first()
        if random_user is None:
            messages.add_message(
                self.request,
                messages.ERROR,
                "You have no users in the database. You can add them "
                "by running python manage.py create_fake_users N "
                "where N is the number of users.",
            )
            return redirect("home")
        form.instance.user = random_user
        form.instance.shortened_url = UrlMapper.get_shortened_url()
        new_url = form.save()
        self._prepare_message(new_url)
        return redirect("result", shortened=new_url.shortened_url)

    def _prepare_message(self, url_object):
        shortened = self._get_shortened_url(url_object)
        message_text = 'Shortened URL address for {0} is <a href="{1}">{1}</a>'
        message = message_text.format(url_object.original_url, shortened)
        messages.add_message(self.request, messages.INFO, message)

    def _get_shortened_url(self, url_object):
        base = settings.BASE_URL
        return "/".join((base, url_object.shortened_url))


def url_redirect(request, shortened=None):
    # TODO: consider handling ftp addresses as well
    original = UrlMapper.objects.get(shortened_url=shortened).original_url
    if original.startswith("http"):
        return redirect(original)
    else:
        return redirect("http://" + original)
