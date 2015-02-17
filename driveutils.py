#! usr/bin/env python

import webbrowser
import os.path
#import . Authenticator

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = None
drive = None
service = None

def findDirectory(service, dirname):
    # title = doesn't work that well for whatever reason
    query = "mimeType = 'application/vnd.google-apps.folder' and title contains '%s'" % dirname 
    files = drive.ListFile({"q" : query}).GetList()
    #so we have to do this to ensure the folder is what we want
    for f in files:
        if file1["tile"] == dirname:
            return f
    return None
    
    
def getDirectoryById(id):
    return drive.CreateFile({"id" : id})
    
def authenticate():
    gauth = GoogleAuth(settings_file="settings.yaml") #settings is broken atm
    if os.path.isfile("creds.json"):
        gauth.LoadCredentialsFile("creds.json")
        gauth.Refresh()
        service = gauth.Authorize()
        
    else:
        auth_url = gauth.GetAuthUrl()
        webbrowser.open(auth_url)
        code = raw_input("Enter your auth code:")
        service = gauth.Auth(code)
        gauth.SaveCredentialsFile("creds.json")

    drive = GoogleDrive(gauth)

def getFiles(dirID):
    query = "mimeType != 'application/vnd.google-apps.folder' and '%s' in parents" % dirID
    files = drive.ListFile({"q": query})
    return files
    
def getOriginalOwnerEmail(fileId,service,email=None):
    permissions = service.permissions().list(fileId=fileId).execute()
    perms1 = permissions.get('items', [])
    for p in perms1:
        if email is None:
            if p["role"] != "owner":
                return p["emailAddress"]
        else:
            if p["emailAddress"] != email:
            return p["emailAddress"]
    return None
    
def test1():
    authenticate()
    getRealOwner("0BwWcaA4Re9t6WVNnejY0VVlRVFU",service)
    
    
if __name__ == "__main__":
    test1()
