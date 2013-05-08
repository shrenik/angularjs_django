#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required,\
#    permission_required
#from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import gettext as _
#from django.conf import settings



def index(request):
    """Index Page"""
    template = 'frontend/index.html'

    data = {

    }
    return render_to_response(template, data,
        context_instance=RequestContext(request))

