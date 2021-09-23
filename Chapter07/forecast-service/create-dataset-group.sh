aws forecast create-dataset-group \
--region eu-west-1 \
--dataset-group-name store_demand_group \
--dataset-arns arn:aws:forecast:eu-west-1:508972911348:dataset/store_demand \
--domain CUSTOM