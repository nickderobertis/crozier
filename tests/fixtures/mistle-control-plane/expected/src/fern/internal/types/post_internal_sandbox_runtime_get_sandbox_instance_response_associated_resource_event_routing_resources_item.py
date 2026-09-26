

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_get_sandbox_instance_response_associated_resource_event_routing_resources_item_message_mode import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItemMessageMode,
)


class PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItem(
    UniversalBaseModel
):
    resource_kind: typing_extensions.Annotated[
        str, FieldMetadata(alias="resourceKind"), pydantic.Field(alias="resourceKind")
    ]
    event_types: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="eventTypes"), pydantic.Field(alias="eventTypes")
    ]
    message_mode: typing_extensions.Annotated[
        typing.Optional[
            PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItemMessageMode
        ],
        FieldMetadata(alias="messageMode"),
        pydantic.Field(alias="messageMode"),
    ] = None
    payload_filter: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="payloadFilter"),
        pydantic.Field(alias="payloadFilter"),
    ] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
