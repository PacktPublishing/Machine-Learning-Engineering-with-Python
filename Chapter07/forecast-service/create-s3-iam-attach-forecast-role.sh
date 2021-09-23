aws iam put-role-policy \
  --role-name ForecastRole \
  --policy-name ForecastBucketAccessPolicy \
  --policy-document '{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "s3:Get*",
            "s3:List*",
            "s3:PutObject"
         ],
         "Resource":[
            "arn:aws:s3:::mleipchapter7",
            "arn:aws:s3:::mleipchapter7/*"
         ]
      }
   ]
}'