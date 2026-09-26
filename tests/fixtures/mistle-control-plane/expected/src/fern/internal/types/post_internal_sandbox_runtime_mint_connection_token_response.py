

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeMintConnectionTokenResponse(UniversalBaseModel):
    instance_id: typing_extensions.Annotated[str, FieldMetadata(alias="instanceId"), pydantic.Field(alias="instanceId")]
    token_jti: typing_extensions.Annotated[str, FieldMetadata(alias="tokenJti"), pydantic.Field(alias="tokenJti")]
    url: str
    token: str
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
