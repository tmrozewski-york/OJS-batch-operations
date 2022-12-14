# OJS-batch-operations
Repo of Python scripts used to batch edit OJS journals via API

## submission stage ID.py ##
Move submissions into stage ID 4 (copyediting). Submissions ingested as part of digitized archives of print journals ingested into older versions of OJS can't be republished after editing because stage ID still shows it's in the submission phase but it needs to be in copyediting. This process *doesn't* assign an editor (assigning participants not currently permitted with API) but that doesn't seem to be a problem (fingers crossed).
