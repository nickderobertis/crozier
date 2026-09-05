

Version = str
"""
Retrieve a snapshot of events from a past time

The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.
"""
