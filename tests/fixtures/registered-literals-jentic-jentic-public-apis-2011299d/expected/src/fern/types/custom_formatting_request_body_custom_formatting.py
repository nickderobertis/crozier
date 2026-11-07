

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomFormattingRequestBodyCustomFormatting(UniversalBaseModel):
    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date format pattern (e.g., `"mm/dd/yyyy"`). See [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting) for more details.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number format pattern (e.g., `"(xxx)xxx-xxxx"`). See [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting) for more details.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email format pattern (e.g., `"username@domain.com"`). See [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
