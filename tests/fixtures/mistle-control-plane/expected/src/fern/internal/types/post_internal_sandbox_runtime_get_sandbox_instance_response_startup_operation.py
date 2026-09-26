

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_get_sandbox_instance_response_startup_operation_operation_kind import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperationOperationKind,
)


class PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperation(UniversalBaseModel):
    operation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="operationId"), pydantic.Field(alias="operationId")
    ]
    operation_kind: typing_extensions.Annotated[
        PostInternalSandboxRuntimeGetSandboxInstanceResponseStartupOperationOperationKind,
        FieldMetadata(alias="operationKind"),
        pydantic.Field(alias="operationKind"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
