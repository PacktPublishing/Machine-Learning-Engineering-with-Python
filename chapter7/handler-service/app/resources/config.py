REGION = 'eu-west-1'
BUCKET_URI = 's3://mleipchapter7/data/rossman/'
ALGORITHM_ARN = 'arn:aws:forecast:::algorithm/Prophet'
PREDICTOR_BASE_NAME = 'store_demand_prophet'#+datetime.datetime.now().strftime(format='%Y_%m_%d')
DATASET_GROUP_ARN = 'arn:aws:forecast:eu-west-1:508972911348:dataset-group/store_demand_group'
DATASET_FREQUENCY = 'D'
FORECAST_BASE_NAME = 'store_model_prophet'