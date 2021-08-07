from flask_restful import Resource, reqparse
from flask import jsonify
import logging

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'store_number',
    type=int,
    required=True,  # need a store
    location="json",
    help='The numerical id of the store'
)

post_parser.add_argument(
    'forecast_start_date',
    type=str,
    location="json",
    help='start date for forecast in iso format YYYY-mm-DDTHH:MM:SS'
)


class ForecastHandler(Resource):
    def __init__(self, **kwargs):
        self.forecaster = kwargs['forecaster']

    def get(self):
        return {}

    def post(self):
        args = post_parser.parse_args()
        print(args)
        result = {"store_number": args["store_number"], "result": self.forecaster.get_forecast(store_id=args["store_number"])}
        return jsonify(result)

import boto3

class Forecaster(object):

    def __init__(self, model_config=None):
        logging.info('Initialising forecaster')
        # Connect API session
        session = boto3.Session(region_name='eu-west-1')
        self._forecast_service = session.client(service_name='forecast')
        self.forecastquery = session.client(service_name='forecastquery')
        forecasts = self._forecast_service.list_forecasts()
        self.forecast_arn = self._forecast_service.list_forecasts()['Forecasts'][0]['ForecastArn']


    def get_forecast(self, store_id=None):
        logging.info('Executing forecast query ...')
        return self.forecastquery.query_forecast(
            ForecastArn=self.forecast_arn,
            Filters={"item_id": str(store_id)}
        )

