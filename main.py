import settings
import datetime
from reddit_submission_diff.differ import Differ
from reddit_submission_diff.mail import sendEmail


submissionHash = settings.SUBMISSION_TO_DIFF

diff = Differ.diff(settings.SUBMISSION_TO_DIFF)

if(diff!=None):
    if(settings.EMAIL_NO_DIFF or diff!=""):

        subject = datetime.datetime.now().strftime("%Y-%m-%d") + " | Diff for: " + settings.SUBMISSION_TO_DIFF
        sendEmail(emailFrom    = settings.EMAIL_FROM,
                  emailTo      = settings.EMAIL_TO,
                  subject      = subject,
                  body         = diff,
                  login        = settings.EMAIL_LOGIN,
                  password     = settings.EMAIL_PASS,
                  smtpServer   = settings.EMAIL_SERVER,
                  smtpPort     = settings.EMAIL_PORT)
else:
    print("HTTP failed to return a submission selftext")
