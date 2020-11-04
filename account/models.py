from django.db import models
from django.views.generic import *


class Wellcome(TemplateView):
   template_name = 'account/../templates/mainapp/Wellcome.html'