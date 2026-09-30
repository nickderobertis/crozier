

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .apple_session_request_user import AppleSessionRequestUser


class AppleSessionRequest(UniversalBaseModel):
    authorization_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="authorizationCode"), pydantic.Field(alias="authorizationCode")
    ]
    id_token: typing_extensions.Annotated[str, FieldMetadata(alias="idToken"), pydantic.Field(alias="idToken")]
    nonce: str
    user: typing.Optional[AppleSessionRequestUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
