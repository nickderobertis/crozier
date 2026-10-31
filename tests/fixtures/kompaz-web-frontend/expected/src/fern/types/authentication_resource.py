

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authentication_resource_token_type import AuthenticationResourceTokenType
from .authentication_resource_user import AuthenticationResourceUser


class AuthenticationResource(UniversalBaseModel):
    token: str
    token_type: typing_extensions.Annotated[
        AuthenticationResourceTokenType, FieldMetadata(alias="tokenType"), pydantic.Field(alias="tokenType")
    ]
    user: AuthenticationResourceUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
