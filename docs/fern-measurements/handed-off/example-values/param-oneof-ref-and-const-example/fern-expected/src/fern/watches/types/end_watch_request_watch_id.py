

import typing

from ...types.watch_id import WatchId
from .end_watch_request_watch_id_one import EndWatchRequestWatchIdOne

EndWatchRequestWatchId = typing.Union[WatchId, EndWatchRequestWatchIdOne]
