

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .totp_type import TotpType


class NonEmptyPasswordCredential(UniversalBaseModel):
    """
    Password credential model for API writes: non-empty username, optionally empty password.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    The password value; may be empty or omitted for logins that have no password
    """

    username: str = pydantic.Field()
    """
    The username associated with the credential (must not be empty)
    """

    totp: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional TOTP (Time-based One-Time Password) string used to generate 2FA codes
    """

    totp_type: typing.Optional[TotpType] = pydantic.Field(default=None)
    """
    Type of 2FA method used for this credential
    """

    totp_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier (email or phone number) used to fetch TOTP codes
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Optional additional password credential metadata fields
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
