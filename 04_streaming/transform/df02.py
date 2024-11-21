#!/usr/bin/env python3

# Copyright 2016 Google Inc.
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

import apache_beam as beam
import logging

logging.basicConfig(level=logging.INFO)


def readline(line):
    import csv
    result = csv.reader([line])
    return next(result)


def extractfields(fields):
    def addtimezone(lat, lon):
        try:
            import timezonefinder
            tf = timezonefinder.TimezoneFinder()
            tz = tf.timezone_at(lng=float(lon), lat=float(lat))
            if tz is None:
                tz = 'UTC'
            return lat, lon, tz
        except ValueError:
            return lat, lon, 'TIMEZONE'  # header

    timezone = addtimezone(fields[21], fields[26])
    return (fields[0], timezone)


def joinfields(f):
    return '{},{}'.format(f[0], ','.join(f[1]))


if __name__ == '__main__':
    with beam.Pipeline('DirectRunner', options=beam.options.pipeline_options.PipelineOptions(
            direct_running_mode='in_memory')) as pipeline:

        airports = (pipeline
                    | beam.io.ReadFromText('airports.csv')
                    | beam.Filter(lambda line: "United States" in line)
                    | beam.Map(readline)
                    | beam.Map(extractfields)
                    )

        airports | beam.Map(joinfields) | beam.io.textio.WriteToText(
            'airports_with_tz')
