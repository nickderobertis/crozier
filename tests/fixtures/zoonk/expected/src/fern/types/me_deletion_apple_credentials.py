

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .apple_session_request import AppleSessionRequest


class MeDeletionAppleCredentials(UniversalBaseModel):
    apple_credentials: typing_extensions.Annotated[
        AppleSessionRequest, FieldMetadata(alias="appleCredentials"), pydantic.Field(alias="appleCredentials")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
