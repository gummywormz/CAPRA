#!/usr/bin/python

import httplib2
import pprint
import webbrowser

from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

def initPermissions():
    CLIENT_ID = "785252251784-bfso0jeq9nv2gr82u7ohl5qf5uctnirj.apps.googleusercontent.com"
    CLIENT_SECRET = "UC86zWuIF8RpH7DyEanQHIjR"

    OAUTH_SCOPE = "https://www.googleapis.com/auth/gmail.compose https://www.googleapis.com/auth/drive.readonly"

    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
	
	# TODO: save credentials in a file??
	
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, 
                            redirect_uri=REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()
    webbrowser.open(authorize_url)
    code = raw_input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    http = httplib2.Http()
    http = credentials.authorize(http)

    drive_service = build('drive', 'v2', http=http)
	
	return drive_service