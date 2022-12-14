'''
DANGER ZONE!
As written, this script will taken everything in your queues and decline it
This was only useful in its current form for the digital archive of a born-print journal: there are no submissions in progress, and all submission in the queues are things that should have been published as submissions in the first place (tables of contents, full issues) or data entry errors
'''

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

# create list of submissions currently in submission queues
# create empty list
z = []
a = requests.get(urlbase + '/submissions', params={'apiToken':token,'status':1,'count':50}).json() # 'status':1 is STATUS_QUEUED (not scheduled, published, or declined)
for item in a['items']:
    z.append(item['id']) # stick all the submission IDs in list z. list is integers
    
# change the status from 1 (queued) to 4 (declined)
# loop through each items in variable z
for i in z:
    b = status_end.replace("{x}",str(i)) # replace placeholder in status_end with submission id as string
    y = requests.put(urlbase + b,params={'apiToken':token},data={'status':4}) # put 'status':4 (STATUS_DECLINED)
    print("submission ID:",i,y) # for logging, print the submission ID and API response
