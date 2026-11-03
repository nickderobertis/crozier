

import typing

from ...types.watch_id import WatchId
from .list_watches_request_scope_zero import ListWatchesRequestScopeZero

ListWatchesRequestScope = typing.Union[ListWatchesRequestScopeZero, WatchId]
