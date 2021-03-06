from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url as r
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, ModelFormMixin

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(TemplateResponseMixin, ModelFormMixin, View):
    template_name = 'subscriptions/subscription_form.html'
    form_class = SubscriptionForm

    def get(self, *args, **kwargs):
        self.object = None
        return self.render_to_response(self.get_context_data())

    def post(self, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if not form.is_valid():
            return self.form_invalid(form)
        return self.form_valid(form)

    def form_valid(self, form):
        #self.object = form.save()

        self.object = Subscription.objects.create(**form.cleaned_data)

        _send_mail('Confirmação de Inscrição',
                   settings.DEFAULT_FROM_EMAIL,
                   self.object.email,
                   'subscriptions/subscription_email.txt',
                   {'subscription': self.object})

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()


new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


