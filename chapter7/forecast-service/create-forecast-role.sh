aws iam create-role \
 --role-name ForecastRole \
 --assume-role-policy-document '{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Principal":{
            "Service":"forecast.amazonaws.com"
         },
         "Action":"sts:AssumeRole"
      }
   ]
}'