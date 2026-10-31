

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_usage_stats_response_collections import GetUsageStatsResponseCollections
from .get_usage_stats_response_files import GetUsageStatsResponseFiles
from .get_usage_stats_response_folders import GetUsageStatsResponseFolders
from .get_usage_stats_response_pastes import GetUsageStatsResponsePastes
from .get_usage_stats_response_shares import GetUsageStatsResponseShares
from .get_usage_stats_response_storage import GetUsageStatsResponseStorage
from .get_usage_stats_response_tokens import GetUsageStatsResponseTokens


class GetUsageStatsResponse(UniversalBaseModel):
    storage: GetUsageStatsResponseStorage
    files: GetUsageStatsResponseFiles
    folders: GetUsageStatsResponseFolders
    pastes: GetUsageStatsResponsePastes
    collections: GetUsageStatsResponseCollections
    shares: GetUsageStatsResponseShares
    tokens: GetUsageStatsResponseTokens

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
