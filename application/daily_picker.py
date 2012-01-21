#!/usr/bin/env python

import sys
import random
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from kanji.models import Kanji

k = random.choice(Kanji.objects.filter(grade__in=[1,2,3,4,5,6], date_used=None))

k.date_used = datetime.date.today()

k.save()
