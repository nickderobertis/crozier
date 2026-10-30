

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filtered_admin_user_collections import FilteredAdminUserCollections
from .filtered_admin_user_files import FilteredAdminUserFiles
from .filtered_admin_user_folders import FilteredAdminUserFolders
from .filtered_admin_user_pastes import FilteredAdminUserPastes
from .filtered_admin_user_shares import FilteredAdminUserShares
from .filtered_admin_user_storage import FilteredAdminUserStorage
from .filtered_admin_user_tokens import FilteredAdminUserTokens
from .filtered_admin_user_type import FilteredAdminUserType


class FilteredAdminUser(UniversalBaseModel):
    id: str
    username: str
    type: FilteredAdminUserType
    storage: typing.Optional[FilteredAdminUserStorage] = None
    files: typing.Optional[FilteredAdminUserFiles] = None
    folders: typing.Optional[FilteredAdminUserFolders] = None
    pastes: typing.Optional[FilteredAdminUserPastes] = None
    collections: typing.Optional[FilteredAdminUserCollections] = None
    shares: typing.Optional[FilteredAdminUserShares] = None
    tokens: typing.Optional[FilteredAdminUserTokens] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
