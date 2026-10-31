

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_admin_usage_response_collections import GetAdminUsageResponseCollections
from .get_admin_usage_response_files import GetAdminUsageResponseFiles
from .get_admin_usage_response_folders import GetAdminUsageResponseFolders
from .get_admin_usage_response_pastes import GetAdminUsageResponsePastes
from .get_admin_usage_response_shares import GetAdminUsageResponseShares
from .get_admin_usage_response_storage import GetAdminUsageResponseStorage


class GetAdminUsageResponse(UniversalBaseModel):
    storage: GetAdminUsageResponseStorage
    files: GetAdminUsageResponseFiles
    folders: GetAdminUsageResponseFolders
    pastes: GetAdminUsageResponsePastes
    collections: GetAdminUsageResponseCollections
    shares: GetAdminUsageResponseShares

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
