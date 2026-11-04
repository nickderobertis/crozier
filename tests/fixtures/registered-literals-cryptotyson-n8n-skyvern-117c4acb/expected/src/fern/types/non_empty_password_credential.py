

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NonEmptyPasswordCredential(UniversalBaseModel):
    """
    Password credential model that requires non-empty values.
    """

    password: str = pydantic.Field()
    """
    The password value (must not be empty)
    """

    username: str = pydantic.Field()
    """
    The username associated with the credential (must not be empty)
    """

    totp: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional TOTP (Time-based One-Time Password) string used to generate 2FA codes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
