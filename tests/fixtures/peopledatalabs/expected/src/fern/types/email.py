

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email_type import EmailType


class Email(UniversalBaseModel):
    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full parsed email
    """

    type: typing.Optional[EmailType] = pydantic.Field(default=None)
    """
    The type of email either current_professional, professional, personal or null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
