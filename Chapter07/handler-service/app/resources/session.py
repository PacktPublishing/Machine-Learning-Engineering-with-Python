from .config import *
import boto3

class ForecastSession(object):

    def __init__(self):
        self.session = boto3.Session(region_name=REGION)
        self.forecast = self.session.client(service_name='forecast')
        self.forecastquery = self.session.client(service_name='forecastquery')