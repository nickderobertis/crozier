

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthSessionUser(UniversalBaseModel):
    id: str
    email: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    email_verified: typing_extensions.Annotated[
        bool, FieldMetadata(alias="emailVerified"), pydantic.Field(alias="emailVerified")
    ]
    email_verified_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="emailVerifiedAt"), pydantic.Field(alias="emailVerifiedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
