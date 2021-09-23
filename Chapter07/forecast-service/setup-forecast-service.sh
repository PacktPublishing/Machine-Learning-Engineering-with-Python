aws forecast create-dataset \
--dataset-name store_demand \
--domain CUSTOM \
--dataset-type TARGET_TIME_SERIES \
--data-frequency D \
--region eu-west-1 \
--schema '{
  "Attributes": [
    {
      "AttributeName": "timestamp",
      "AttributeType": "timestamp"
    },
    {
      "AttributeName": "target_value",
      "AttributeType": "integer"
    },
    {
      "AttributeName": "item_id",
      "AttributeType": "string"
    }
  ]
}'