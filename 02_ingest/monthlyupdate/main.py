#!/usr/bin/env python

# Copyright 2016-2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from markupsafe import escape
from ingest_flights import ingest, next_month
import functions_framework
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()


@functions_framework.http
def ingest_flights(request):
    """HTTP Cloud Function
    Args:
            request (flask.Request): The request object
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
            Returns:
                            The response text, or any set of values that can be turned into a
                            Response object using `make_response`
                            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    try:
        logging.basicConfig(
            format='%(levelname)s: %(message)s', level=logging.INFO)
        json = request.get_json(force=True)

        year = escape(json['year']) if 'year' in json else None
        month = escape(json['month']) if 'month' in json else None
        bucket = escape(json['bucket'])  # required

        if year is None or month is None or len(year) == 0 or len(month) == 0:
            year, month = next_month(bucket)
        logging.debug('Ingesting year={} month={}'.format(year, month))
        tableref, numrows = ingest(year, month, bucket)
        ok = 'Success ... ingested {} rows to {}'.format(
            numrows, tableref)
        logging.info(ok)
        return ok
    except Exception as e:
        logging.exception("Failed to ingest ... try again later?")
        return "Failure", 500
