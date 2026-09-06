

import typing

from ...types.c_published_file_get_details_response import CPublishedFileGetDetailsResponse
from ...types.config_detail_response import ConfigDetailResponse

GetV1SteamFiledetailsResponse = typing.Union[ConfigDetailResponse, CPublishedFileGetDetailsResponse]
