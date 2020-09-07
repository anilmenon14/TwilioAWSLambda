# Integration of Twilio WhatsaApp API to AWS lambda

## Purpose: Notification via AWS Lambda for Cloudwatch event of Auto Scaling events to trigger a WhatsApp notification

## Pre-requisites:
  - Install serverless-python-requirements serverless plugin to ensure serverless knows of requirements
  - Set up Twilio account and have Account SID, Auth Token, 'from' number (i.e. Twilion sandbox) and 'to' numbers (i.e. subscribed receivers)
  - Create a config.dev.json file under 'config' directory. Refer to config.template.json for format.


`serverless plugin install -n serverless-python-requirements`
