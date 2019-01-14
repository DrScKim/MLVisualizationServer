from django_extensions.management.jobs import BaseJob
#from django_extensions.management.jobs import HourlyJob
from django_extensions.management.jobs import MinutelyJob


from django.test import TestCase

class Job(BaseJob):
    help = "Base Job"

    def execute(self):
        # executing empty sample job
        pass