

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_permissions_grant_context_data_item import ContextPermissionsGrantContextDataItem
from .context_permissions_grant_files_item import ContextPermissionsGrantFilesItem
from .context_permissions_grant_vector_stores_item import ContextPermissionsGrantVectorStoresItem


class ContextPermissionsGrant(UniversalBaseModel):
    files: typing.Optional[typing.List[ContextPermissionsGrantFilesItem]] = None
    vector_stores: typing.Optional[typing.List[ContextPermissionsGrantVectorStoresItem]] = None
    context_data: typing.Optional[typing.List[ContextPermissionsGrantContextDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
