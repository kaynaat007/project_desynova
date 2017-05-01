from django_cron import CronJobBase, Schedule
from django.core.cache import cache
import requests
from rest_framework import status


def load_data_from_server():
    try:
        looser_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json'
        gainer_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json'
        urls = {
            'gainer': gainer_url,
            'loser': looser_url
        }
        for key, url in urls.iteritems():
            response = requests.get(url)
            if not response.status_code == status.HTTP_200_OK:
                raise Exception("Error in fetching data from url {0} ".format(url), response.reason)
            top_ten_users_data = response.json()['data']
            cache.set(key, top_ten_users_data, timeout=None)
        print "success"
        # hit api
    except Exception as e:
        raise Exception("error in cron job", e.args or e.message)


