import difflib
import requests
import json
import os.path

class Differ:

  def diff(submissionHash):
    #Grab old text
    fileName = submissionHash + ".txt"
    filePath = "storage/" + fileName
    if(os.path.isfile(filePath)):
        oldVersionFile = open(filePath, "r")
        oldSubmission = oldVersionFile.readlines()
        oldVersionFile.close()
    else:
        oldSubmission = ""

    #Grab new text
    url = "http://www.reddit.com/" + submissionHash + "/.json"

    submissionResponse = requests.get(url)

    #If successful
    if(submissionResponse.ok):
        submissionJson = json.loads(submissionResponse.content)

        newVersion = submissionJson[0]["data"]["children"][0]["data"]["selftext_html"]
        diff = difflib.unified_diff(oldSubmission, newVersion)
        diffString = '\n'.join(diff)

        #Save new version if edits exist
        if(len(diffString)>0):
          newVersionFile = open(filePath, "w")
          newVersionFile.write(newVersion)
          newVersionFile.close()
          return diffString


    return None
