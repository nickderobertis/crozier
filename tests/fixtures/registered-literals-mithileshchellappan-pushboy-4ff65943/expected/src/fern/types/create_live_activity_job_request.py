

import typing

from .live_activity_end_job_request import LiveActivityEndJobRequest
from .live_activity_start_job_request import LiveActivityStartJobRequest
from .live_activity_update_job_request import LiveActivityUpdateJobRequest

CreateLiveActivityJobRequest = typing.Union[
    LiveActivityStartJobRequest, LiveActivityUpdateJobRequest, LiveActivityEndJobRequest
]
