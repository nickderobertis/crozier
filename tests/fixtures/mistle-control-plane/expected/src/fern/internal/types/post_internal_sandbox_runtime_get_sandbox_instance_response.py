

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_get_sandbox_instance_response_associated_resource_event_routing import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRouting,
)
from .post_internal_sandbox_runtime_get_sandbox_instance_response_startup_operation import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperation,
)
from .post_internal_sandbox_runtime_get_sandbox_instance_response_status import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus,
)


class PostInternalSandboxRuntimeGetSandboxInstanceResponse(UniversalBaseModel):
    id: str
    status: PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus
    failure_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="failureCode"), pydantic.Field(alias="failureCode")
    ] = None
    failure_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="failureMessage"), pydantic.Field(alias="failureMessage")
    ] = None
    sandbox_profile_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sandboxProfileId"), pydantic.Field(alias="sandboxProfileId")
    ]
    sandbox_profile_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="sandboxProfileVersion"), pydantic.Field(alias="sandboxProfileVersion")
    ]
    startup_operation: typing_extensions.Annotated[
        typing.Optional[PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperation],
        FieldMetadata(alias="startupOperation"),
        pydantic.Field(alias="startupOperation"),
    ] = None
    associated_resource_event_routing: typing_extensions.Annotated[
        typing.Optional[PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRouting],
        FieldMetadata(alias="associatedResourceEventRouting"),
        pydantic.Field(alias="associatedResourceEventRouting"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
