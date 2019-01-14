from django_extensions.management.jobs import BaseJob
from django_extensions.management.jobs import HourlyJob



class Job(HourlyJob):
    help = "logging time for every hourly"

    def execute(self):
        # executing empty sample job
        with open('./log/hourly.log','a') as fp:
            print('logging local time')
            import time
            now = time.localtime()
            s = "%04d-%02d-%02d %02d:%02d:%02d\n" % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

            fp.write(s)


