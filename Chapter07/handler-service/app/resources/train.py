from flask_restful import Resource, reqparse
from flask import jsonify
from .config import *
import datetime
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
    'train_request_date',
    type=str,
    location="json",
    help="Date of training request - normally today's date but allow for time travel from user. Format: YYYY-mm-DDTHH:MM:SS"
)


class TrainingHandler(Resource):
    def __init__(self, **kwargs):
        self.forecaster = kwargs['forecaster']

    def get(self):
        return {}

    def post(self):
        args = post_parser.parse_args()
        print(args)
        result = {"store_number": args["store_number"], "result": self.forecaster.forecast()}
        return jsonify(result)


class Trainer(object):

    def __init__(self, forecast_session):
        self.forecast_session = forecast_session
        self.df_pred_metadata = self.get_df_pred_metadata()
        self.latest_predictor = self.get_latest_predictor()

    def get_df_pred_metadata(self):
        predictor_metadata = self.forecast_session.forecast.list_predictors()['Predictors']
        df_pred_metadata = pd.DataFrame.from_records(predictor_metadata)
        return df_pred_metadata

    def get_latest_predictor(self):
        latest_predictor = self.df_pred_metadata.sort_values(by='CreationTime', ascending=False).loc[0].to_dict()
        return latest_predictor

    def latest_predictor_in_tolerance(self, tolerance_days=2):
        train_time_elapsed_days = (
                datetime.datetime.now() - self.latest_predictor['CreationTime'].replace(tzinfo=None)
        ).days
        if train_time_elapsed_days < tolerance_days:
            return True
        else:
            return False

    def train_new_predictor(self):
        PREDICTOR_NAME = PREDICTOR_BASE_NAME + datetime.datetime.now().strftime(format='%Y_%m_%d_%H_%M')
        train_response = self.forecast_session.forecast.create_predictor(PredictorName=PREDICTOR_NAME,
                                                                         AlgorithmArn=ALGORITHM_ARN,
                                                                         ForecastHorizon=7,
                                                                         PerformAutoML=False,
                                                                         PerformHPO=False,
                                                                         InputDataConfig={
                                                                             "DatasetGroupArn": DATASET_GROUP_ARN},
                                                                         FeaturizationConfig={
                                                                             "ForecastFrequency": DATASET_FREQUENCY}
                                                                         )
        return train_response

    def create_latest_forecast(self):
        FORECAST_NAME = FORECAST_BASE_NAME + datetime.datetime.now().strftime(format='%Y_%m_%d_%H_%M')
        create_forecast_response = self.forecast_session.forecast.create_forecast(
            ForecastName=FORECAST_NAME,
            PredictorArn=self.latest_predictor['PredictorArn'])
        return create_forecast_response
