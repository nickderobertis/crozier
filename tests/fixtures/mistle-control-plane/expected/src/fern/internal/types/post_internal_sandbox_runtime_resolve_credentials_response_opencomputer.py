

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_credentials_response_opencomputer_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseOpencomputerSource,
)


class PostInternalSandboxRuntimeResolveCredentialsResponseOpencomputer(UniversalBaseModel):
    source: PostInternalSandboxRuntimeResolveCredentialsResponseOpencomputerSource
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    api_base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiBaseUrl"), pydantic.Field(alias="apiBaseUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
