#!/bin/bash

# same as in setup_svc_acct
NAME=ingest-flights-monthly
SVC_ACCT=svc-monthly-ingest
PROJECT_ID=$(gcloud config get-value project)
REGION=us-central1
SVC_EMAIL=${SVC_ACCT}@${PROJECT_ID}.iam.gserviceaccount.com

# Deploy as cloud function
gcloud functions deploy $NAME \
    --entry-point ingest_flights --runtime python311 --trigger-http \
    --timeout 720s --service-account ${SVC_EMAIL} --no-allow-unauthenticated \
		--memory 500MiB

# Deploy as Docker container - Deprecated, moved to Cloud Function
# gcloud run deploy $NAME --region $REGION --source=$(pwd) \
#    --platform=managed --service-account ${SVC_EMAIL} --no-allow-unauthenticated \
#    --timeout 12m \

