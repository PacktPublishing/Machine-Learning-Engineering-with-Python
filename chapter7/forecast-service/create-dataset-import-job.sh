aws forecast create-dataset-import-job \
--region eu-west-1 \
--dataset-arn arn:aws:forecast:eu-west-1:508972911348:dataset/store_demand \
--dataset-import-job-name store_demand_job \
--data-source '{
    "S3Config": {
      "Path": "s3://mleipchapter7/data/rossman/train-prepared.csv",
      "RoleArn": "arn:aws:iam::508972911348:role/ForecastRole"
    }
  }'