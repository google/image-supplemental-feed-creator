# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gspread
import json
import os

gc = gspread.service_account(filename='credentials.json')
config = json.load(open('./config.json'))

def create_or_update_spreadsheet(event, context):
  try:
    sheet_name = config['sheet_name']
    try:
      sh = gc.open(sheet_name)
      worksheet = sh.get_worksheet(0)
    except gspread.exceptions.SpreadsheetNotFound:
      sh = gc.create(sheet_name)

      for user in config['users']:
        sh.share(user['email'], perm_type='user', role=user['role'])
        worksheet = sh.get_worksheet(0)
        worksheet.update('A1', "id")
        worksheet.update('B1', "image_url")

    print(f"Processing file: {event['name']}.")
    worksheet.append_row(values=[event['name'], f"https://storage.googleapis.com/{event['bucket']}/{event['name']}"])
  except Exception as ex:
    print(f"Failed to create or update spreadsheet. See exception for details: {ex}")
