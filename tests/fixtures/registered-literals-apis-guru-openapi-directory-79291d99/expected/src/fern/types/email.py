

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email_type import EmailType


class Email(UniversalBaseModel):
    """
    An object representing an email address
    """

    data: str = pydantic.Field()
    """
    The email address.
    """

    primary: bool = pydantic.Field()
    """
    When `true`, identifies the email address as the primary email on an account.
    """

    type: EmailType = pydantic.Field()
    """
    The type of email account as described by the financial institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
