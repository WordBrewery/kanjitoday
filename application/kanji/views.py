from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import date
from kanji.models import *

def frontpage(request):
    todays_kanji = Kanji.objects.get(date_used=date.today())
    return render_to_response('index.html', {'todays_kanji': todays_kanji}, context_instance = RequestContext(request))
