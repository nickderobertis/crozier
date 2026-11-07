

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomFormattingRequestBodyCustomFormatting(UniversalBaseModel):
    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date format pattern (e.g., `"mm/dd/yyyy"`)
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number format pattern (e.g., `"(xxx)xxx-xxxx"`)
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email format pattern (e.g., `"username@domain.com"`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
