

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_credentials_response_modal_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseModalSource,
)


class PostInternalSandboxRuntimeResolveCredentialsResponseModal(UniversalBaseModel):
    source: PostInternalSandboxRuntimeResolveCredentialsResponseModalSource
    token_id: typing_extensions.Annotated[str, FieldMetadata(alias="tokenId"), pydantic.Field(alias="tokenId")]
    token_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="tokenSecret"), pydantic.Field(alias="tokenSecret")
    ]
    app_name: typing_extensions.Annotated[str, FieldMetadata(alias="appName"), pydantic.Field(alias="appName")]
    environment: typing.Optional[str] = None
    default_timeout_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="defaultTimeoutMs"), pydantic.Field(alias="defaultTimeoutMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
