

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vault_connection_list_connections_item_provider import VaultConnectionListConnectionsItemProvider
from .vault_connection_list_connections_item_resolution_mode import VaultConnectionListConnectionsItemResolutionMode
from .vault_connection_list_connections_item_status import VaultConnectionListConnectionsItemStatus


class VaultConnectionListConnectionsItem(UniversalBaseModel):
    id: str
    provider: VaultConnectionListConnectionsItemProvider
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    resolution_mode: typing_extensions.Annotated[
        VaultConnectionListConnectionsItemResolutionMode,
        FieldMetadata(alias="resolutionMode"),
        pydantic.Field(alias="resolutionMode"),
    ]
    status: VaultConnectionListConnectionsItemStatus
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
