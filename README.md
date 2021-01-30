# Image Supplemental Feed Creator

## Description

This project is a collection of templates for files to be added to a Google Cloud function.

Files included:
- `main.py`
- `requirements.txt`
- `config.json`
- `credentials.json`

## Pre-requisites

- A Google Cloud Project
- A service account with credentials.json file downloaded
- A Google Cloud Function with `Python 3.8` runtime
- Email ids that will need to access the generated spreadsheet

## File contents to be replaced

### `config.json`
- Add email ids here for anyone that will need to access the generated spreadsheet
- Provide a role to each user, either `reader` or `writer`
- Ensure that there is atleast one `writer`

### `credentials.json`
Replace the entire contents of this file with the contents of the JSON file downloaded for your service account
