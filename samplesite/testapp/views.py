from django.views.generic import ListView
from .models import SMS

class SMSListView(ListView):
    model = SMS
    template_name = 'testapp/sms_list.html'
    context_object_name = 'sms_list'