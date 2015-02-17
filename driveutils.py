#! usr/bin/env python

import webbrowser
import os.path
#import . Authenticator

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = None
drive = None

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
    service = None
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
    getRealOwner("0BwWcaA4Re9t6WVNnejY0VVlRVFU",service)
    drive = GoogleDrive(gauth)

def getFiles(dirID):
    query = "mimeType != 'application/vnd.google-apps.folder' and '%s' in parents" % dirID
    files = drive.ListFile({"q": query})
    return files
    
def getRealOwner(fileId,service):
    permissions = service.permissions().list(fileId=fileId).execute()
    perms1 = permissions.get('items', [])
    for p in perms1:
        if p["role"] != "owner":
            print p["emailAddress"]
    
def test1():
    authenticate()
    
    
if __name__ == "__main__":
    test1()