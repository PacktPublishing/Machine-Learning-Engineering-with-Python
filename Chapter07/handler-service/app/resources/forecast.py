from flask_restful import Resource, reqparse
from flask import jsonify
import logging
import pandas as pd

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


class Forecaster(object):

    def __init__(self, forecast_session):
        self.forecast_session = forecast_session
        self.df_forecast_metadata = self.get_df_forecast_metadata()
        self.latest_forecast = self.get_latest_forecast()

    def get_df_forecast_metadata(self):
        forecast_metadata = self.forecast_session.forecast.list_forecasts()['Forecasts']
        df_forecast_metadata = pd.DataFrame.from_records(forecast_metadata)
        return df_forecast_metadata

    def get_latest_forecast(self):
        latest_forecast = self.df_forecast_metadata.sort_values(by='CreationTime', ascending=False).loc[0].to_dict()
        return latest_forecast

    def get_forecast(self, store_id):
        return self.forecast_session.forecastquery.query_forecast(
            ForecastArn=self.latest_forecast['ForecastArn'],
            Filters={"item_id": str(store_id)}
        )

