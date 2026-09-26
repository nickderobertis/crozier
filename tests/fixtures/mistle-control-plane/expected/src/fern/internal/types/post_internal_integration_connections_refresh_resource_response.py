

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_integration_connections_refresh_resource_response_sync_state import (
    PostInternalIntegrationConnectionsRefreshResourceResponseSyncState,
)


class PostInternalIntegrationConnectionsRefreshResourceResponse(UniversalBaseModel):
    connection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    family_id: typing_extensions.Annotated[str, FieldMetadata(alias="familyId"), pydantic.Field(alias="familyId")]
    kind: str
    sync_state: typing_extensions.Annotated[
        PostInternalIntegrationConnectionsRefreshResourceResponseSyncState,
        FieldMetadata(alias="syncState"),
        pydantic.Field(alias="syncState"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
