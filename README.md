# OJS-batch-operations
Repo of Python scripts used to batch edit OJS journals via API

## submission stage ID.py ##
Move submissions into stage ID 4 (copyediting). Submissions ingested as part of digitized archives of print journals ingested into older versions of OJS can't be republished after editing because stage ID still shows it's in the submission phase but it needs to be in copyediting. This process *doesn't* assign an editor (assigning participants not currently permitted with API) but that doesn't seem to be a problem (fingers crossed).

## decline subs queue.py ##
Returns a list of all submissions in the submission queues then declines those submissions. This instance of OJS is the digital archive of a born-print journal so there are only submissions in the queues if we unpublished things that shouldn't have been published as submissions (ToCs, full issues (which we harvested and reposted as issue galleys)) or due to user error from ingest efforts. If you want to batch decline submissions when there are legitimate submissions in the queues, you don't want to use the first GET call to populate list z - instead, you want to manually populate list z (either in the script or a text file) and loop through the specified submission IDs.

## month start and end dates.py ##
OJS API often wants start and end dates in YYYY-MM-DD format as ranges for extracting historical stats. It takes as input two variables: start_date and end_date (date strings in YYYY-MM-DD format) and outputs a 3-column data frame with the month (YYYY-MM), month start (YYYY-MM-DD), and month end (YYYY-MM-DD) for each month in the range. Uses pandas and calendar.
