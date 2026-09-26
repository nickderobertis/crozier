

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resolve_credentials_response_e2b_source import (
    PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource,
)


class PostInternalSandboxRuntimeResolveCredentialsResponseE2B(UniversalBaseModel):
    source: PostInternalSandboxRuntimeResolveCredentialsResponseE2BSource
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    domain: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
