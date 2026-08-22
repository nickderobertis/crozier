

import typing

from .filter_changes_response_hashes import FilterChangesResponseHashes
from .filter_logs_response import FilterLogsResponse

FilterChangesResponse = typing.Union[FilterLogsResponse, FilterChangesResponseHashes]
