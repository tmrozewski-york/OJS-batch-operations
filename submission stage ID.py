# load libraries
import os
import requests

# working directory
my_dir = ' ' # set WD here
os.chdir(my_dir)

# API token
token = ' ' # API token here

# API endpoint
# The full endpoint will be concatenated from urlbase and status_end with the placeholders replace
# For more recent YDJ journals in OJS, the second {journal} placeholder is "default," not a repeat of the journal subdomain
urlbase = 'https://{journal}.journals.yorku.ca/index.php/{journal}/api/v1/' # root URL for API requests - in this format to facilitate code reuse
journal = ' ' # set the journal subdomain here
a = urlbase.replace('{journal}',journal) # create a usable root for the URL
status_end = '/submissions/{submissionId}' # format for the API endpoint
b = [] # enter submission IDs you want to edit as strings in this list

# Edit the submission stage ID
# loops through each item variable b
for i in b:
    c = status_end.replace("{submissionId}",i) # replace the placeholder in status_end with the submission ID
    y = requests.put(b + c,params={'apiToken':token},data={'stageId':4}) # PUT request in API, setting submission stage ID to 4 (copyediting)
    print("submission ID:",i,y) # for logging, print the submission ID and API response
