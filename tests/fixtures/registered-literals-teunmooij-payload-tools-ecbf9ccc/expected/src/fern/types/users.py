

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Users(UniversalBaseModel):
    id: str
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    email: typing.Optional[str] = None
    reset_password_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resetPasswordToken"), pydantic.Field(alias="resetPasswordToken")
    ] = None
    reset_password_expiration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resetPasswordExpiration"),
        pydantic.Field(alias="resetPasswordExpiration"),
    ] = None
    salt: typing.Optional[str] = None
    hash: typing.Optional[str] = None
    login_attempts: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="loginAttempts"), pydantic.Field(alias="loginAttempts")
    ] = None
    lock_until: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lockUntil"), pydantic.Field(alias="lockUntil")
    ] = None
    password: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
