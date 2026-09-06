

import typing

from ...types.api_response import ApiResponse
from ...types.backup_data import BackupData

DumpdataResponse = typing.Union[ApiResponse, BackupData]
